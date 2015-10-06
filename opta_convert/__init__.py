import sys
import csv
from lxml import etree

def convert_id(opta_id):
    'DFL-OBJ-0000XT'
    suffix = opta_id.split('-')[-1]
    return int(suffix, 36)


def player_id(elem):
    if elem.get('TeamId') == 'Ball':
        return 0

    return convert_id(elem.get('PersonId'))

def team_id(elem):
    team = elem.get('TeamId')
    if team == 'Ball':
        return 0
    return convert_id(team)


def convert(xml_path, csv_path):
    with open(xml_path) as fobj:
        with open(csv_path, 'w') as outfile:
            pos_writer = csv.writer(outfile)

            context = etree.iterparse(fobj)

            for _, elem in context:
                if elem.tag == 'FrameSet':
                    # print elem.attrib
                    player = player_id(elem)
                    team = team_id(elem)
                    
                    match = convert_id(elem.get('MatchId'))
                    period = 1+ (elem.get('GameSection') == 'secondHalf')

                    for n, frame in enumerate(elem):
                        #to centi seconds (1/100 s)
                        time = n*4
                        x = frame.get('X')
                        y = frame.get('Y')

                        #last 0 for velocity
                        pos_writer.writerow([match, period, time, player, team, x, y, 0])

                    elem.clear()

def main():
    args = sys.argv[1:]
    if len(args) < 2:
        sys.stderr.write('Usage: opta_convert.py in.xml out.csv\n')
    else:
        convert(args[0], args[1])


if __name__ == '__main__':
    main()

