# Student RAG Assistant

## Description
A basic Retrieval-Augmented Generation (RAG) style system that:
- Takes user query
- Retrieves relevant student data
- Builds context
- Generates response

## Features
- Query-based filtering (above, below, top)
- Dynamic number handling (e.g., "above 75", "below 60")
- Modular code structure (functions)
- JSON-based data storage

## How to run
python main.py

## Example Queries
- show students above 80
- show students above 75
- show students below 90
- who is top

## How it Works
1. User enters a query
2. System extracts number (if present)
3. Retrieves matching students
4. Builds context
5. Generates final response