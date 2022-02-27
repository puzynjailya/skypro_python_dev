from flask import Blueprint, render_template, Flask

catalog_blueprint = Blueprint('catalog_blueprint',
                              __name__,
                              template_folder='templates')


@catalog_blueprint.route('/catalog/')
def catalog_page():
    return render_template('main.html')


@catalog_blueprint.route('/catalog/<cat>')
def category_page(cat):
    return render_template('category.html', category=cat)


@catalog_blueprint.route('/catalog/<int:item>')
def item_page(item):
    return render_template('item.html', item=item)