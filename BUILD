load("@pip_deps//:requirements.bzl", "requirement")
load("@rules_python//python/pip_install:requirements.bzl", "compile_pip_requirements")

py_library(
  name = "candle_pipeline",
  srcs = ["candle_pipeline.py"],
  deps = [
    requirement("apache-beam"),
  ],
)

py_test(
  name = "candle_pipeline_test",
  srcs = ["candle_pipeline_test.py"],
)

compile_pip_requirements(
    name = "requirements",
    extra_args = ["--allow-unsafe"],
    requirements_in = "requirements.txt",
    requirements_txt = "requirements_lock.txt",
)
