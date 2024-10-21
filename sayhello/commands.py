import click
from sayhello import app, db
from sayhello.models import Message
#初始化数据库
@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    if drop:
        db.drop_all()
        click.echo('Succssfully deleted the current database.')
    db.create_all()
    click.echo('Initialized database.')
#生成虚拟数据，可选是否清空原数据库
@app.cli.command()
@click.option('--count', default=5, help='Quantity of messages, default is 5.')
@click.option('--drop', is_flag=True, help='Whether to clear the original database when generating new data.')
def forge(count, drop):
    if drop:
        db.drop_all()
    from faker import Faker
    fake = Faker()
    db.create_all()
    click.echo('Working...')

    for _ in range(count):
        message = Message(
            name=fake.name(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year()
        )
        db.session.add(message)
    db.session.commit()
    click.echo(f'Created {count} fake messages.')
    