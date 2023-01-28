load("@pip_deps//:requirements.bzl", "requirement")
load("@rules_python//python/pip_install:requirements.bzl", "compile_pip_requirements")

py_library(
    name = "main",
    srcs = ["main.py"],
    deps = [
        requirement("apache-beam"),
    ],
)

py_test(
    name = "main_test",
    srcs = ["main_test.py"],
    deps = [
        ":candle_pipeline",
    ],
)

compile_pip_requirements(
    name = "requirements",
    requirements_in = "requirements.txt",
    requirements_txt = "requirements_lock.txt",
)
