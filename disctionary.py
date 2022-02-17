


data = {
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}

print(data['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossTerm'])
print(data['glossary']['GlossDiv']['GlossList']['GlossEntry']['Abbrev'])    

#XML
print(data['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossDef']['GlossSeeAlso'][1])

print(data['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossSee'])



