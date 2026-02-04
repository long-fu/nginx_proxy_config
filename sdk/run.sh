#!/bin/bash
uvicorn channel_info:app --host 0.0.0.0 --port 24902 --workers 1