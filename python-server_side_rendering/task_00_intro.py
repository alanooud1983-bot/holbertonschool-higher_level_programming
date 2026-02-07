def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    if template.strip() == "":
        print("Template is empty, no output files generated")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    for index, person in enumerate(attendees, start=1):
        name = person.get("name", "N/A")
        title = person.get("event_title", "N/A")
        date = person.get("event_date", "N/A")
        location = person.get("event_location", "N/A"

        output_text = template.format(
            name=name,
            event_title=title,
            event_date=date,
            event_location=location
        )

        filename = f"output_{index}.txt"
        with open(filename, "w") as f:
            f.write(output_text)
