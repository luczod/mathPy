'''
https://docs.astral.sh/uv/pip/packages/#editable-packages
uv init projectname
uv add matplotlib
uv sync
uv pip compile pyproject.toml -o requirements.txt

'''

def main():
    print("Hello from mathpy!")


if __name__ == "__main__":
    main()
