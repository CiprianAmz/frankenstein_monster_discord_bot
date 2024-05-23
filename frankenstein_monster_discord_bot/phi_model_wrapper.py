import onnxruntime_genai as og


class PhiModelWrapper():
    # inspired from https://github.com/Azure-Samples/Phi-3MiniSamples/blob/main/onnx/run-onnx.ipynb

    def __init__(self, model_folder_path: str, prompt_prefix: str) -> None:
        self._model = og.Model(model_folder_path)
        self._tokenizer = og.Tokenizer(self._model)
        self._tokenizer_stream = self._tokenizer.create_stream()

        search_options = {"max_length": 512, "temperature": 0.6}
        self._params = og.GeneratorParams(self._model)
        self._params.try_graph_capture_with_max_batch_size(0)
        self._params.set_search_options(**search_options)

        self._prompt_prefix = prompt_prefix

    def reply(self, message: str) -> str:
        prompt = f"<|user|>{self._prompt_prefix} \n {message}<|end|><|assistant|>"
        input_tokens = self._tokenizer.encode(prompt)
        self._params.input_ids = input_tokens

        generator = og.Generator(self._model, self._params)

        response: str = ""
        while not generator.is_done():
            generator.compute_logits()
            generator.generate_next_token()

            new_token = generator.get_next_tokens()[0]
            response += self._tokenizer_stream.decode(new_token)

        return response
