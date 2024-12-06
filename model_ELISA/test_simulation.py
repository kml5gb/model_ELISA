import unittest
from unittest.mock import MagicMock
import tkinter as tk
from model_ELISA_gui import insert_default_parameters, clear_plot_and_inputs, run_simulation
import model_ELISA_gui  # This imports the module where FigureCanvasTkAgg is used

class TestElisaSimulation(unittest.TestCase):
    def setUp(self):
        # Mock entry widgets
        self.mock_entries = {key: MagicMock() for key in [
            "capture_entry", "antigen_entry", "detection_entry",
            "substrate_entry", "k_on1_entry", "k_off1_entry",
            "k_on2_entry", "k_off2_entry", "k_cat1_entry",
            "k_cat2_entry", "overall_time_entry"
        ]}

        # Mock the plot frame
        self.mock_plot_frame = MagicMock()

        # Mock FigureCanvasTkAgg to avoid any Tkinter interactions
        self.mock_figure_canvas = MagicMock()
        self.mock_figure_canvas.get_tk_widget.return_value = MagicMock()

        # Mock FigureCanvasTkAgg in the model_ELISA_gui module
        model_ELISA_gui.FigureCanvasTkAgg = MagicMock(return_value=self.mock_figure_canvas)

    def tearDown(self):
        # Restore original FigureCanvasTkAgg after tests
        del model_ELISA_gui.FigureCanvasTkAgg

    def test_insert_default_parameters(self):
        insert_default_parameters(self.mock_entries)
        for key, mock_entry in self.mock_entries.items():
            mock_entry.delete.assert_called_with(0, tk.END)
            mock_entry.insert.assert_called_once()

    def test_clear_plot_and_inputs(self):
        clear_plot_and_inputs(self.mock_entries, self.mock_plot_frame)
        self.mock_plot_frame.winfo_children.assert_called()
        for mock_entry in self.mock_entries.values():
            mock_entry.delete.assert_called_with(0, tk.END)

    def test_run_simulation(self):
        for key, mock_entry in self.mock_entries.items():
            mock_entry.get.return_value = "10"  # Mock valid inputs

        # Run the simulation with mocked Tkinter widgets
        run_simulation(
            self.mock_entries["capture_entry"], self.mock_entries["antigen_entry"],
            self.mock_entries["detection_entry"], self.mock_entries["substrate_entry"],
            self.mock_entries["k_on1_entry"], self.mock_entries["k_off1_entry"],
            self.mock_entries["k_on2_entry"], self.mock_entries["k_off2_entry"],
            self.mock_entries["k_cat1_entry"], self.mock_entries["k_cat2_entry"],
            self.mock_entries["overall_time_entry"], self.mock_plot_frame
        )

        # Check that the canvas creation method is called but doesn't interact with actual widgets
        self.mock_figure_canvas.get_tk_widget.assert_called()
        self.mock_plot_frame.winfo_children.assert_called()
        print("Test run_simulation passed!")

if __name__ == "__main__":
    unittest.main()
