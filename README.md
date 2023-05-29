# dynamic_context

Extension for oobabooga's [Text Generation WebUI](https://github.com/oobabooga/text-generation-webui) that replaces the tags {{time}},  {{date}} and {{weekday}} in the character's context with the current time, and date, respectively.
Additionally it also adds the current time as extra information at the end of the prompt (and optionally the date too).

This is a simple extension, and this additional context doesn't get saved in the chat history, as it's purpose is only to bias the AI response while keeping in mind the current time, or date.
