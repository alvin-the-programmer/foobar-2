def solution(total_lambs):
    return max_henchmen_when_stingy(total_lambs) - max_henchmen_when_generous(total_lambs)


def max_henchmen_when_generous(total_lambs):
    curr_cost = 1
    henchmen = []
    while total_lambs >= curr_cost:
        total_lambs -= curr_cost
        henchmen.append(curr_cost)
        curr_cost *= 2
    return len(henchmen)


def max_henchmen_when_stingy(total_lambs):
    curr_cost = 1
    henchmen = []
    while total_lambs >= curr_cost:
        total_lambs -= curr_cost
        henchmen.append(curr_cost)
        if len(henchmen) != 1:
            curr_cost = henchmen[-1] + henchmen[-2]
    return len(henchmen)

