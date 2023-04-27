from jinja2 import Template


def craft_template(template_string: str, context: dict):
    template = Template(template_string)
    content = template.render(context)
    return content
