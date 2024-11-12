import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from unittest import mock
from dashboard import plot_temperature_trends

@pytest.fixture
def mock_st_pyplot(mocker):
    # Mock streamlit.pyplot for verification
    return mocker.patch('streamlit.pyplot')

@pytest.fixture
def mock_plt(mocker):
    # Mock plt as it is imported in dashboard.py
    return mocker.patch('dashboard.plt')

def test_plot_temperature_trends_data_processing(mock_st_pyplot, mock_plt):
    # Test data
    days = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"]
    max_temps = [20, 22, 21, 19, 23, 24, 22]
    min_temps = [15, 16, 15, 14, 17, 18, 16]

    # Call the function
    plot_temperature_trends(days, max_temps, min_temps)

    # Verify that data is processed and plot() is called correctly
    assert mock_plt.plot.called, "plot() should have been called for max and min temperatures"
    assert mock_st_pyplot.called, "st.pyplot() should have been called to render the plot"

    # Check that the data passed to plot() is correct
    mock_plt.plot.assert_any_call(days, max_temps, label="Max Temp (°C)", marker='o', linestyle='-', color='red')
    mock_plt.plot.assert_any_call(days, min_temps, label="Min Temp (°C)", marker='o', linestyle='-', color='blue')

    print("Test for plot_temperature_trends data processing was successful")
