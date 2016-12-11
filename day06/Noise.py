from collections import Counter


class Noise:
    def get_message(self, data, required):
        message, echos = "", [list(x) for x in data.split("\n")]
        for x in range(0, len(echos[0])):
            temp = []
            for echo in echos:
                temp.append(echo[x])
            message += Counter(temp).most_common()[required][0]
        return message
