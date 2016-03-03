//Для каждого языка программирования вычислите количество успешных посылок на этом языке. 

import collections
languages = collections.Counter()

for line in sys.stdin:
    name, letter, time, lang, res = line.rstrip().split("\t")
    if res == "OK":
        languages[lang] += 1

result = []
pairs = [[languages[key], key] for key in languages]
pairs.sort(reverse=True)

if len(pairs) != 0:
    max_freq = pairs[0][0]

    for freq, language in pairs:
        if freq == max_freq:
            result.append([language, freq])
        else:
            for l, f in sorted(result):
                print(l, f)
            result = []
            result.append([language, freq])
            max_freq = freq
    else:
        for l, f in sorted(result):
            print(l, f)