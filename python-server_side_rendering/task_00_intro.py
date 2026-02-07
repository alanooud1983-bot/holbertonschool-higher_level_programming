def generate_invitations(template, attendees):
    # 1. Validate input types
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # 2. Handle empty template
    if template.strip() == "":
        print("Template is empty, no output files generated")
        return

    # 3. Handle empty attendees list
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # 4. Process each attendee
    for index, person in enumerate(attendees, start=1):
        name = person.get("name", "N/A")
        event_title = person.get("event_title", "N/A")
        event_date = person.get("event_date", "N/A")
        event_location = person.get("event_location", "N/A")

        # 5. Replace placeholders
        output_text = template.format(
            name=name,
            event_title=event_title,
            event_date=event_date,
            event_location=event_location
        )

        # 6. Write output file
        filename = f"output_{index}.txt"
        with open(filename, "w") as f:
            f.write(output_text)
