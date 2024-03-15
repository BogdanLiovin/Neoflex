import sqlite3 as sq
def db_start():
    global db, cur
    db=sq.connect("my_db.db", check_same_thread=False)
    cur=db.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS profile(user_id TEXT PRIMARY KEY,FullName TEXT, emaill TEXT, password TEXT,'
                ' JobTitle TEXT, points TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS product(product_id TEXT PRIMARY KEY, ProductName TEXT, ProductType TEXT,'
                ' ProductCost TEXT, ProductDescription TEXT, ProductImage TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS challenge(challenge_id TEXT PRIMARY KEY, ChallengeName TEXT,'
                ' Reward TEXT, ChallengeDescription TEXT, ChallengeType TEXT)')
    db.commit()
def create_profile(user_id):
    user=cur.execute('SELECT 1 FROM profile WHERE user_id=="{key}"'.format(key=user_id)).fetchone()

    if not user:
        cur.execute('INSERT INTO profile VALUES(?,?,?,?,?,?)',
                    (user_id,'','','','',''))
        db.commit()
def edit_profile(state, user_id):
    cur.execute('UPDATE profile SET FullName ="{}",emaill="{}", password="{}", JobTitle="{}",'
                ' points="{}" WHERE user_id =="{}"'.format(
        state['FullName'],state['email'],state['password'],state['JobTitle'],state['points'],  user_id))
    db.commit()

def create_product(product_id):
    product=cur.execute('SELECT 1 FROM product WHERE product_id=="{key}"'.format(key=product_id)).fetchone()
    if not product:
        cur.execute('INSERT INTO product VALUES(?,?,?,?,?,?)',
                    (product_id,'','','','',''))
        db.commit()

async def edit_product(data, product_id):
    cur.execute('UPDATE product SET ProductName ="{}", ProductType="{}", ProductCost="{}", ProductDescription="{}",'
                'ProductImage="{}" WHERE product_id =="{}"'.format(
        data['ProductName'],data['ProductType'],data['ProductCost'],data['ProductDescription'], data['ProductImage'], product_id))
    db.commit()

def create_challenge(challenge_id):
    challenge=cur.execute('SELECT 1 FROM challenge WHERE challenge_id=="{key}"'.format(key=challenge_id)).fetchone()
    if not challenge:
        cur.execute('INSERT INTO challenge VALUES(?,?,?,?,?)',
                    (challenge_id,'','','',''))
        db.commit()
def edit_challenge(data, challenge_id):
    cur.execute('UPDATE challenge SET ChallengeName ="{}", Reward="{}", ChallengeDescription="{}", '
                'ChallengeType="{}" WHERE challenge_id =="{}"'.format(
        data['ChallengeName'],data['Reward'],data['ChallengeDescription'],data['ChallengeType'], challenge_id))
    db.commit()
