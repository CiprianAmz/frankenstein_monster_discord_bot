#!/usr/bin/bash

git lfs install
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx
cd Phi-3-mini-4k-instruct
git reset --hard 5fa3419