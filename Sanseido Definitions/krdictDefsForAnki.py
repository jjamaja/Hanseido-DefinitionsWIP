#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
	Korean Definitions plugin for Anki
	pulls definitions from https://krdict.korean.go.kr/

	Forked from kqueryful's Sanseido-Definitions


	Definition fetching adapted from rikaichan.js
	Field updating modified from Sentence_Gloss.py
	@author		= wezurii
	@author		= jjamaja
	@date 		= 14/12/2017
	@version 	= 1.0
"""
from bs4.BeautifulSoup import BeautifulSoup
import urllib
import re

# Edit these field names if necessary ==========================================
expressionField = 'Word'
definitionField = 'Sanseido'
# ==============================================================================

# Fetch definition from Sanseido ===============================================
def fetchDef(term):
	defText = ""
	pageUrl = "https://krdict.korean.go.kr/dicSearch/search?mainSearchWord=" + urllib.quote(term.encode('utf-8'))
	response = urllib.urlopen(pageUrl)
	soup = BeautifulSoup(response)
	NetDicBody = soup.find('span', class_ = "base_t")

	if NetDicBody != None:
		defFinished = False

		for line in NetDicBody.children:
			if line.name == "b":
				if len(line) != 1:
					for child in line.children:
						if child.name == "span":
							defFinished = True
			if defFinished:
				break

			if line.string != None and line.string != u"\n":
				defText += line.string

	defText = re.sub(ur"［(?P<no>[２-９]+)］", ur"<br/><br/>［\1］", defText)
	return re.sub(ur"（(?P<num>[２-９]+)）", ur"<br/>（\1）", defText)

# Update note ==================================================================
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from anki.hooks import addHook
from anki.notes import Note
from aqt import mw

def glossNote( f ):
   if f[ definitionField ]: return
   f[ definitionField ] = fetchDef( f[ expressionField ] )

def setupMenu( ed ):
	a = QAction( 'Regenerate Korean definitions', ed )
	ed.connect( a, SIGNAL('triggered()'), lambda e=ed: onRegenGlosses( e ) )
	ed.form.menuEdit.addAction( a )

def onRegenGlosses( ed ):
	n = "Regenerate Korean definitions"
	ed.editor.saveNow()
	regenGlosses(ed, ed.selectedNotes() )
	mw.requireReset()

def regenGlosses( ed, fids ):
	mw.progress.start( max=len( fids ) , immediate=True)
	for (i,fid) in enumerate( fids ):
		mw.progress.update( label='Generating Korean definitions...', value=i )
		f = mw.col.getNote(id=fid)
		try: glossNote( f )
		except:
			import traceback
			print 'definitions failed:'
			traceback.print_exc()
		try: f.flush()
		except:
			raise Exception()
		ed.onRowChanged(f,f)
	mw.progress.finish()

addHook( 'browser.setupMenus', setupMenu )
