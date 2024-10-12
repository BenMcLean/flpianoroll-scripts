import ast
import astor # pip install astor
import os
import shutil
from typing import List
import winreg

def read_registry_str(full_path: str) -> str:
	key_parts: List[str] = full_path.split("\\")
	value_name: str = key_parts.pop()
	key_path: str = "\\".join(key_parts)
	root_key_str: str
	sub_key: str
	root_key_str, sub_key = key_path.split("\\", 1)
	try:
		root_key: int = getattr(winreg, root_key_str)
	except AttributeError:
		raise ValueError(f"Invalid root key: \"{root_key_str}\"")
	with winreg.OpenKey(root_key, sub_key) as key:
		key: winreg.HKEYType
		value: str
		value, _ = winreg.QueryValueEx(key, value_name)
		return value

class ImportModifier(ast.NodeTransformer):
	def visit_ImportFrom(self, node: ast.ImportFrom) -> ast.ImportFrom:
		if node.module == '.flpianoroll':
			node.module = 'flpianoroll'
		return node

	def visit_Import(self, node: ast.Import) -> ast.Import:
		for alias in node.names:
			if alias.name == '.flpianoroll':
				alias.name = 'flpianoroll'
		return node

def modify_imports(content: str) -> str:
	tree: ast.Module = ast.parse(content)
	modifier: ImportModifier = ImportModifier()
	modified_tree: ast.Module = modifier.visit(tree)
	modified_content: str = astor.to_source(modified_tree)
	return modified_content

def copy_and_replace(source_path, destination_path):
	if os.path.exists(destination_path):
		os.remove(destination_path)
	shutil.copy2(source_path, destination_path)

SOURCE_PATH: str = 'src'
FLPIANOROLL_SCRIPTS_PATH: str = os.path.join(
	read_registry_str(r"HKEY_CURRENT_USER\Software\Image-Line\Shared\Paths\Shared data"),
	r"FL Studio\Settings\Piano roll scripts")

for filename in os.listdir(SOURCE_PATH):
	if filename == 'flpianoroll.py':
		continue
	elif filename.endswith('.py'):
		with open(os.path.join(SOURCE_PATH, filename), 'r') as f:
			content = f.read()
		fileDestinationPath: str = os.path.join(FLPIANOROLL_SCRIPTS_PATH, filename.replace('.py', '.pyscript'))
		with open(fileDestinationPath, 'w') as f:
			f.write(modify_imports(content))
		print(f'Deployed \"{filename}\" to \"{fileDestinationPath}\".')
	else:
		fileDestinationPath: str = os.path.join(FLPIANOROLL_SCRIPTS_PATH, filename)
		copy_and_replace(os.path.join(SOURCE_PATH, filename), fileDestinationPath)
		print(f'Deployed \"{filename}\" to \"{fileDestinationPath}\".')
