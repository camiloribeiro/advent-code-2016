from collections import Counter


class Noise:
    def get_most_repeated_char(self, data):
        message, echos = "", [list(x) for x in data.split("\n")]
        for x in range(0, len(echos[0])):
            temp = []
            for echo in echos:
                temp.append(echo[x])
            message += Counter(temp).most_common(1)[0][0]
        return message
