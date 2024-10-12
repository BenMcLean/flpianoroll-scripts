from typing import Any, Callable, List, Optional

class Marker:
	mode: int
	name: str # marker name
	scale_helper: str # (scale markers only) comma-separated string, representing note classes from C through to B, with '0' for in scale and '1' for out of scale. E.g. C# Major (Ionian) would have scale_helper '1,0,1,0,1,0,0,1,0,1,0,0'
	scale_root: int # (scale markers only) note class of the scale's tonic, with C as 0
	time: float # ticks
	tsden: int # when marker is a time signature
	tsnum: int # when marker is a time signature

class Note:
	clone: Callable # duplicate note/s
	color: int # 0 to 15, default 0. Color group / MIDI channel.
	fcut: float # 0.0 to 1.0, default 0.5
	fres: float # 0.0 to 1.0, default 0.5
	group: int # group number this note belongs to
	length: float # ticks
	muted: bool
	number: int # note number (MIDI standard)
	pan: float # 0.0 to 1.0, default 0.5
	pitchofs: int # -120 to 120
	porta: bool
	release: float # 0.0 to 1.0
	repeats: int
	selected: bool
	slide: bool
	time: float # ticks
	velocity: float # 0.0 to 1.0, default 0.8

class Pattern:
	PPQ: int
	addMarker: Callable
	addNote: Callable
	clear: Callable
	clearMarkers: Callable
	clearNotes: Callable
	deleteMarker: Callable
	deleteNote: Callable
	getDefaultNoteProperties: Callable
	getMarker: Callable
	getNextFreeGroupIndex: Callable
	getNote: Callable
	getTimelineSelection: Callable
	length: float
	markerCount: int
	noteCount: int
	snap_root_note: Any
	snap_scale_helper: Any
	tsden: int
	tsnum: int

class ScriptDialog:
	def __init__(self, Title: str, Description: str):
		"""
		Initialize a new ScriptDialog.

		Args:
			Title (str): The title of the dialog.
			Description (str): The description or content of the dialog.
		"""
		...

	def AddInput(self, aName: str, Value: Any) -> None:
		"""
		Adds a generic input control.

		Args:
			aName (str): The name of the input control.
			Value (Any): The initial value of the input control.
		"""
		...

	def AddInputKnob(self, aName: str, Value: float, Min: float, Max: float) -> None:
		"""
		Adds a knob input control with floating point value.

		Args:
			aName (str): The name of the knob control.
			Value (float): The initial value of the knob.
			Min (float): The minimum value of the knob.
			Max (float): The maximum value of the knob.
		"""
		...

	def AddInputKnobInt(self, aName: str, Value: int, Min: int, Max: int) -> None:
		"""
		Adds a knob input control with integer value.

		Args:
			aName (str): The name of the knob control.
			Value (int): The initial value of the knob.
			Min (int): The minimum value of the knob.
			Max (int): The maximum value of the knob.
		"""
		...

	def AddInputCombo(self, aName: str, ValueList: List[str], Value: str) -> None:
		"""
		Adds a combobox input control.

		Args:
			aName (str): The name of the combobox control.
			ValueList (List[str]): The list of options for the combobox.
			Value (str): The initial selected value in the combobox.
		"""
		...

	def AddInputText(self, aName: str, Value: str) -> None:
		"""
		Adds a text input control.

		Args:
			aName (str): The name of the text input control.
			Value (str): The initial text value.
		"""
		...

	def AddInputCheckbox(self, aName: str, Value: bool) -> None:
		"""
		Adds a checkbox input control with boolean value.

		Args:
			aName (str): The name of the checkbox control.
			Value (bool): The initial state of the checkbox (True for checked, False for unchecked).
		"""
		...

	def GetInputValue(self, aName: str) -> Any:
		"""
		Retrieve the current value of the input with the specified name.

		Args:
			aName (str): The name of the input control to retrieve the value from.

		Returns:
			Any: The current value of the specified input control.
		"""
		...

	def Execute(self) -> bool:
		"""
		Show the dialog.

		Returns:
			bool: True if the user pressed OK, False if the dialog was cancelled.
		"""
		...

	SetText: Callable
	addInput: Callable
	addInputCheckbox: Callable
	addInputCombo: Callable
	addInputKnob: Callable
	addInputKnobInt: Callable
	addInputSurface: Callable
	addInputText: Callable
	execute: Callable
	getInputValue: Callable
	restoreFormValues: Callable
	setText: Callable

class score:
	"""Use the global variable 'score' to access these functions"""
	PPQ: int  # ticks per quarter note (read-only)
	tsnum: int  # current project time signature numerator (read-only)
	tsden: int  # current project time signature denominator (read-only)
	
	@staticmethod
	def clear(all: Optional[bool] = None) -> None:
		"""Remove notes and markers. Specify "True" to clear all, instead of just selected."""
		...

	@staticmethod
	def clearNotes(all: Optional[bool] = None) -> None:
		"""Remove notes. Specify "True" to clear all, instead of just selected."""
		...

	@staticmethod
	def clearMarkers(all: Optional[bool] = None) -> None:
		"""Remove markers. Specify "True" to clear all, instead of just selected."""
		...

	noteCount: int  # nr of notes (read-only)

	@staticmethod
	def addNote(note: Any) -> None:
		"""Add new note"""
		...

	@staticmethod
	def getNote(index: int) -> Any:
		"""Get note"""
		...

	@staticmethod
	def deleteNote(index: int) -> None:
		"""Delete the indexed note"""
		...

	markerCount: int  # nr of markers (read-only)

	@staticmethod
	def addMarker(marker: Any) -> None:
		"""Add new marker"""
		...

	@staticmethod
	def getMarker(index: int) -> Any:
		"""Get markers index"""
		...

	@staticmethod
	def deleteMarker(index: int) -> None:
		"""Delete the indexed marker"""
		...

class TUtils:
	@staticmethod
	def ProgressMsg(Msg: str, Pos: int, Total: int) -> None:
		"""
		Shows a progress message.

		Args:
			Msg (str): The message to display.
			Pos (int): The current position in the progress.
			Total (int): The total number of steps or items.
		"""
		...

	@staticmethod
	def ShowMessage(Msg: str) -> None:
		"""
		Shows a message in a dialog box.

		Args:
			Msg (str): The message to display in the dialog box.
		"""
		...

	@staticmethod
	def log(Msg: str) -> None:
		"""
		Writes a string to the FL Studio debug log tab.

		Args:
			Msg (str): The message to write to the debug log.
		"""
		...

class Utils:
	"""Use global variable "Utils" to access these functions"""
	@staticmethod
	def ShowMessage(message: str) -> None:
		"""Displays a message as entered."""
		...
