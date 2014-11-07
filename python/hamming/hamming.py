def distance(strand_1, strand_2):
	hamming_distance = 0

	strand_1 = strand_1.strip()
	strand_2 = strand_2.strip()

	longer = strand_1 if len(strand_1) > len(strand_2) else strand_2
	shorter = strand_1 if len(strand_1) <= len(strand_2) else strand_1

	for i in range(len(shorter)):
		if shorter[i] != longer[i]:
			hamming_distance += 1

	hamming_distance += len(longer) - len(shorter)

	return hamming_distance