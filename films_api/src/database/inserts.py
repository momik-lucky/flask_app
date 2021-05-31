from datetime import date

from src.app import db
from src.database.models import Film, Actor


def populate_films():
    harry_potter_and_ph_stone = Film(
        title='Harry Potter and the Philosopher\'s Stone',
        release_date=date(2001, 11, 4),
        description='An aaaaaaaa aaaaa aaaaaaaa aaaaaaa',
        distributed_by='Warner Bros. Pictures',
        length=161,
        rating=7.6,
    )
    harry_potter_and_ch_s = Film(
        title='Harry Potter and the Ch S',
        release_date=date(2002, 11, 3),
        description='An aaaaaaaa aaaaa aaaaaaaa aaaaaaa',
        distributed_by='Warner Bros. Pictures',
        length=161,
        rating=7.4,
    )
    harry_potter_and_priz_az = Film(
        title='Harry Potter and the Priz Az',
        release_date=date(2004, 6, 4),
        description='An aaaaaaaa aaaaa aaaaaaaa aaaaaaa',
        distributed_by='Warner Bros. Pictures',
        length=161,
        rating=7.9,
    )
    harry_potter_and_ph_goblet_fire = Film(
        title='Harry Potter and the Goblet Fire',
        release_date=date(2005, 11, 6),
        description='An aaaaaaaa aaaaa aaaaaaaa aaaaaaa',
        distributed_by='Warner Bros. Pictures',
        length=161,
        rating=7.6,
    )
    harry_potter_and_order_phoenix = Film(
        title='Harry Potter and the Order Phoenix',
        release_date=date(2007, 7, 19),
        description='An aaaaaaaa aaaaa aaaaaaaa aaaaaaa',
        distributed_by='Warner Bros. Pictures',
        length=161,
        rating=7.6,
    )
    harry_potter_and_half_blood_prince = Film(
        title='Harry Potter and the Half-Blood Prince',
        release_date=date(2001, 11, 4),
        description='An aaaaaaaa aaaaa aaaaaaaa aaaaaaa',
        distributed_by='Warner Bros. Pictures',
        length=161,
        rating=7.6,
    )
    harry_potter_and_deathly_hallows_1 = Film(
        title='Harry Potter and the Deathly Hallows part 1',
        release_date=date(2001, 11, 4),
        description='An aaaaaaaa aaaaa aaaaaaaa aaaaaaa',
        distributed_by='Warner Bros. Pictures',
        length=161,
        rating=7.6,
    )
    harry_potter_and_deathly_hallows_2 = Film(
        title='Harry Potter and the Deathly Hallows part 2',
        release_date=date(2001, 11, 4),
        description='An aaaaaaaa aaaaa aaaaaaaa aaaaaaa',
        distributed_by='Warner Bros. Pictures',
        length=161,
        rating=7.6,
    )

    daniel_radcliffe = Actor(name='Daniel Radcliffe', birthday=date(1989, 7, 23), is_active=True)
    emma_watson = Actor(name='Emma Watson', birthday=date(1990, 4, 15), is_active=True)
    rupert_grint = Actor(name='Rupert Grint', birthday=date(1988, 9, 24), is_active=True)
    richard_harris = Actor(name='Richard Harris', birthday=date(1939, 10, 1), is_active=True)
    michael_gambon = Actor(name='Michael Gambon', birthday=date(1940, 10, 19), is_active=True)
    alan_rickman = Actor(name='Alan Rickman', birthday=date(1946, 2, 21), is_active=True)

    db.session.add(harry_potter_and_ph_stone)
    db.session.add(harry_potter_and_ch_s)
    db.session.add(harry_potter_and_priz_az)
    db.session.add(harry_potter_and_ph_goblet_fire)
    db.session.add(harry_potter_and_order_phoenix)
    db.session.add(harry_potter_and_half_blood_prince)
    db.session.add(harry_potter_and_deathly_hallows_1)
    db.session.add(harry_potter_and_deathly_hallows_2)

    db.session.commit()
    db.session.close()


if __name__ == '__main__':
    print('Populating db...')
    populate_films()
    print('Successfully populated!')
