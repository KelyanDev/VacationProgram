from main import Vacances, ADECalendar
import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='VacationProgram', size=(1000,480))
        #Définition des caractéristiques de l'interface (Taille, position, texte, etc...)
        self.panel = wx.Panel(self)
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.liste = self.import_list_box()
        self.txt = "Choisissez un enseignant:"
        self.font_choix = wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.DEFAULT)
        self.font_result = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.DEFAULT)
        self.st = wx.StaticText(self.panel, label=self.txt, style=wx.ALIGN_LEFT)
        self.st.SetFont(self.font_choix)
        self.retour = wx.StaticText(self.panel, label='Vacances',)
        self.retour.SetFont(self.font_result)
        self.liste_cb = self.list_box()
        
        #Bouton de confirmation
        self.confirm = wx.Button(self.panel, label='Confirmer')
        self.confirm.Bind(wx.EVT_BUTTON, self.renvoi_vacances)

        #Ajout des widgets dans l'interface
        self.main_sizer.Add(self.st, 0, wx.ALL | wx.CENTER)
        self.main_sizer.Add(self.liste_cb, 0, wx.ALL | wx.CENTER, 5)
        self.main_sizer.Add(self.confirm, 0, wx.ALL | wx.CENTER, 5)
        self.main_sizer.AddStretchSpacer()
        self.main_sizer.Add(self.retour, 0, wx.ALL)
        self.main_sizer.AddStretchSpacer()
        self.panel.SetSizer(self.main_sizer)
        self.Show()
        
    #Importation de la liste des Enseignants
    def import_list_box(self):
        self.edt = ADECalendar.copy()
        liste = Vacances.liste_enseignants(self)
        return liste

    #Définition de la boite de choix
    def list_box(self):
        boite = wx.ComboBox(self.panel, pos=(50,50), choices=self.liste, style=wx.CB_READONLY)
        return boite
    
    #Renvoi les periodes de vacances
    def renvoi_vacances(self, event):
        resultat = Vacances(str(self.liste_cb.GetValue()))
        self.retour.SetLabel(f'''Toussaint: {resultat.toussaint} \n\n Décembre:{resultat.decembre} \n\n Hiver: {resultat.hiver} \n\n Printemps: {resultat.printemps} \n\n Ete: {resultat.ete}''')
        

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()