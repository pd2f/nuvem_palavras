#!/usr/bin/env python
# coding: utf-8

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import spacy

class  Nuvem:
    def __init__(self):
        self.wordcloud = None
        self.titulo = None
        self.descricao = None
        self.doc = None
        self.votos = None
        self.color = "white"
        self.texto = ''
        self.pln = spacy.load('pt_core_news_sm')
        self.classes_gramaticais = ['ADJ','ADP','PUNCT','ADV','AUX','SYM','INTJ','CONJ','X','NOUN','DET','PROPN','NUM','VERB','PART','PRON','SCONJ']
        
    def set_documento(self, array_textos):
        self.doc = array_textos
        self.texto_normalizado()
    
    def set_color(self,color):
        self.color = color
        
    def set_votos(self, array_votos):
        self.votos = array_votos

    def set_texto(self,texto):
        self.doc = [texto]
        self.texto_normalizado()
    
    def set_classes_gramaticais(self,array_classes_gramaticais):
        self.classes_gramaticais = array_classes_gramaticais
        
    def generate(self):
        self.wordcloud = WordCloud(max_font_size=50, background_color=self.color).generate(self.texto)
        
    def show_jupiter(self):
        self.generate()
        plt.figure()
        plt.imshow(self.wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show()

    def show_popup(self):
        self.generate()
        image = self.wordcloud.to_image()
        image.show()
    
    ''' Função para incluir uma frase para cada voto de um post-it'''
    def replicar_votos(self):
        votos_efeito = []
        pos = 0
        for voto in self.votos:
            loop = int(voto)
            while loop > 0:
                loop -=1
                votos_efeito.append(self.doc[pos])
            pos +=1
        self.set_documento(votos_efeitos)
        
    
    ''' Função para seleção de classe gramatical'''
    def texto_normalizado(self):
        texto_pln = None
        for doc in self.doc:
            texto_pln = self.pln(doc)
            for palavra in texto_pln:
                if  palavra.pos_ in self.classes_gramaticais:
                    if not palavra.is_stop:
                        if palavra.pos_ == "VERB":
                            self.texto += " "+str(palavra.lemma_)
                        else:
                            self.texto += " "+str(palavra.text)