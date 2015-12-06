from bottle import static_file, route, run, view, template
import os

@route("/static/<filename>")
def serve_file(filename):
    return static_file(filename, root="./")

@route("/")
def directory():
    content = os.listdir("./")
    directory = []
    for item in content:
        if ".png" in item:
            directory.append(item)
    template_str = """
    %for item in directory:
    <img src="/static/{{item}}/><br/>
    %end
    """
    return template(template_str, directory=directory)


if __name__ == "__main__":
    run(host="0.0.0.0", port="8080", debug=True)
