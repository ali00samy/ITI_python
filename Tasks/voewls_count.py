def voewls_count(word):
    voewls = "aeiouAEIOU"
    count = 0

    for char in word:
        if char in voewls:
            count += 1

    print(f"Voewls count: {count}")
