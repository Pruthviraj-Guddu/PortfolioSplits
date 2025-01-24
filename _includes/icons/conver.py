import xml.etree.ElementTree as ET

def convert_svg(input_file, output_file):
    # Parse the input SVG file
    tree = ET.parse(input_file)
    root = tree.getroot()

    # Create the new SVG structure
    new_svg = ET.Element("svg", {
        "id": "identicon",
        "xmlns": "http://www.w3.org/2000/svg",
        "viewBox": "0 0 160 32"
    })
    title = ET.SubElement(new_svg, "title")
    title.text = "Pruthviraj"

    # Define a function to generate lines from a path
    def parse_path_to_lines(path_data, color):
        commands = path_data.split(" ")
        lines = []
        for i in range(0, len(commands) - 1, 2):
            try:
                x1, y1 = map(float, commands[i][1:].split(","))
                x2, y2 = map(float, commands[i + 1].split(","))
                line = ET.Element("line", {
                    "x1": str(x1 / 10), "y1": str(y1 / 50),
                    "x2": str(x2 / 10), "y2": str(y2 / 50),
                    "stroke": color,
                    "stroke-width": "2"
                })
                lines.append(line)
            except:
                continue
        return lines

    # Iterate through path elements in the input SVG
    for path in root.findall(".//{http://www.w3.org/2000/svg}path"):
        fill_color = path.get("fill", "black")
        path_data = path.get("d", "")
        lines = parse_path_to_lines(path_data, fill_color)
        for line in lines:
            new_svg.append(line)

    # Write the new SVG to the output file
    new_svg_tree = ET.ElementTree(new_svg)
    new_svg_tree.write(output_file, encoding="utf-8", xml_declaration=True)

# Example usage
input_file = "pruthviraj-guddu.svg"  # Replace with your input SVG file path
output_file = "output.svg"  # Replace with your desired output SVG file path
convert_svg(input_file, output_file)
