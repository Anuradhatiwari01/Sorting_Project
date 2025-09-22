# SortVision - Sorting Algorithm Visualizer & Analyzer (FastAPI Edition)

SortVision is a full-stack web application designed for visualizing, understanding, and benchmarking common sorting algorithms. It provides an interactive frontend built with vanilla HTML, CSS, and JavaScript, and a powerful **Python FastAPI backend** for high-performance analysis.

![demo](https://i.imgur.com/example.gif)
*(To generate a `demo.gif`, you can use a screen recording tool like [LiceCap](https://www.cockos.com/licecap/) or [ScreenToGif](https://www.screentogif.com/) to capture the visualization and benchmarking process.)*

## Features

- **Interactive Visualization:** Watch algorithms sort an array step-by-step with highlights for comparisons and swaps.
- **Playback Controls:** Start, pause, resume, step-through, and reset the visualization.
- **Multiple Algorithms:** Bubble, Selection, Insertion, Merge, Quick, Heap, and Counting Sort.
- **Dataset Generation:** Generate random, sorted, reverse-sorted, or nearly-sorted arrays.
- **CSV Upload:** Upload your own dataset from a single-column CSV file.
- **Performance Analyzer:** Run server-side benchmarks using a high-performance FastAPI backend.
- **Data-driven Results:** View benchmark results (time, comparisons, swaps) in both a table and a chart.
- **CSV Export:** Download the results of your benchmark analysis as a CSV file.
- **Algorithm Theory:** A handy panel displays the time and space complexity for the selected algorithm.

## Setup and Installation

### Prerequisites

- Python 3.8+
- `pip` and `venv`

### 1. Clone the Repository

```bash
git clone <repository-url>
cd sort-vision-fastapi