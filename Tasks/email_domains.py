def get_domains(emails):
    domains = [email.split("@")[1] for email in emails if "@" in email]

    print(set(domains))
