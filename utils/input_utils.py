import inspect


def input_wrapper(func):
    def wrapper():
        params = inspect.signature(func).parameters

        args = []
        for param_name, param in params.items():
            value = input(
                f"'{param_name}' ({param.annotation if param.annotation != param.empty else 'any type'}): "
            )

            try:
                if param.annotation != param.empty:
                    converted_value = param.annotation(value)
                else:
                    converted_value = value

                args.append(converted_value)
            except (ValueError, TypeError) as e:
                print(
                    f"It's not possible to convert {param_name} to {param.annotation} : {e}"
                )
                raise

        return func(*args)

    return wrapper
