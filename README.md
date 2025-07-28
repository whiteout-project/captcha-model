# Captcha Model

This repository hosts our in-house trained captcha model, using over 80,000 captcha images gathered from bots.

# Size

The model is only `13.2 MB` (`12.6 MiB`) in size, which is only **25%** of the size of [ddddocr](https://github.com/sml2h3/ddddocr)'s `common.onnx` model, which is `54.1 MB` (`51.58 MiB`).

# Accuracy

When testing the model using a dataset of 950 labeled captcha images (not used in training), it achieved an accuracy of **81.79%** (`777/950`).

For comparison, [ddddocr](https://github.com/sml2h3/ddddocr) only managed to achieve an accuracy of **69.68%** (`662/950`).

# Speed

Compared to [ddddocr](https://github.com/sml2h3/ddddocr), our model takes `41.7ms`[^1] to solve a captcha, which is `28.3ms` slower than ddddocr's `13.4ms`[^2] per captcha.

Although slower, that difference is negligible and will not be noticable.

# Usage

View the [example](example.py) on how to use the model.

[^1]: Measured on a `2019 16" Macbook Pro` with an `Intel i7-9750H`
[^2]: Also measured on the same hardware