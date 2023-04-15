# https://pypi.org/project/wikipedia/
import wikipedia

wikipedia.set_lang("es")
print(wikipedia.summary("Boole"))


# Wikipedia (/ˌwɪkɨˈpiːdiə/ or /ˌwɪkiˈpiːdiə/ WIK-i-PEE-dee-ə) is a collaboratively edited, multilingual, free Internet encyclopedia supported by the non-profit Wikimedia Foundation...

# wikipedia.search("Barack")
# print("Barack")
#[u'Barak (given name)', u'Barack Obama', u'Barack (brandy)', u'Presidency of Barack Obama', u'Family of Barack Obama', u'First inauguration of Barack Obama', u'Barack Obama presidential campaign, 2008', u'Barack Obama, Sr.', u'Barack Obama citizenship conspiracy theories', u'Presidential transition of Barack Obama']

# ny = wikipedia.page("New York")
# ny.title
# u'New York'
# ny.url
# u'http://en.wikipedia.org/wiki/New_York'
# ny.content
# u'New York is a state in the Northeastern region of the United States. New York is the 27th-most exten'...
# ny.links[0]
# u'1790 United States Census'

#wikipedia.set_lang("es")
#wikipedia.summary("Facebook", sentences=1)
# Facebook est un service de réseautage social en ligne sur Internet permettant d'y publier des informations (photographies, liens, textes, etc.) en contrôlant leur visibilité par différentes catégories de personnes.
