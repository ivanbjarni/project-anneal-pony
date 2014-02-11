pnl = wx.Panel(self)
        
        wx.StaticBox(pnl, label='Sparnaður', pos=(5, 5), size=(550, 100))

        fe_merki = wx.StaticText(pnl, label = 'Lausafé:', pos = (20, 40))
        fe_reitur = wx.TextCtrl(pnl, value = '', size = (60, 20), pos = (20, 65))

        manadarlega_merki = wx.StaticText(pnl, label = 'Manaðarlega:', pos = (100, 40))
        manadarlega_reitur = wx.ListBox(pnl, pos = (100, 65), choices = ['ja', 'nei'], size = (40, 20))

        timabil_merki = wx.StaticText(pnl, label = 'Í hve marga mánuði?', pos = (190, 40))
        timabil_reitur = wx.TextCtrl(pnl, value = '', size = (60, 20), pos = (190, 65))


        wx.StaticBox(pnl, label = 'Lán', pos = (5, 110), size = (550, 245))

        lan_nafn_merki = wx.StaticText(pnl, label = 'Nafn:', pos = (20, 150))
        lan_nafn_reitur1 = wx.TextCtrl(pnl, value = '', size = (90, 20), pos = (20, 175))

        lan_vedtrygg_merki = wx.StaticText(pnl, label = 'Verdtr.:', pos = (130, 150))
        lan_vedtrygg_reitur1 = wx.ListBox(pnl, pos = (130, 175), choices =['ja', 'nei'], size = (40, 20))

        lan_eftirstodvar_merki = wx.StaticText(pnl, label = 'Eftirstöðvar:', pos = (190, 150))
        lan_eftirstodvar_reitur1 = wx.TextCtrl(pnl, value = '', size = (70, 20), pos = (190, 175))

        lan_vextir_merki = wx.StaticText(pnl, label = 'Vextir:', pos = (280, 150))
        lan_vextir_reitur1 = wx.TextCtrl(pnl, value = '', size = (40, 20), pos = (280, 175))

        lan_afborgar_merki = wx.StaticText(pnl, label = 'Afborgarnir eftir:', pos = (350, 150))
        lan_afborgar_reitur1 = wx.TextCtrl(pnl, value = '', size = ( 70, 20), pos = (350, 175))

        verdbolga_merki = wx.StaticText(pnl, label = 'Verðbólgatímabil: ', pos = (20, 325))
        verdbolga_fyrribil = wx.TextCtrl(pnl, value = '', size = (60, 20), pos = (125, 325))
        verdbolga_strik = wx.StaticText(pnl, label = ' - ', pos = (195, 325))
        verdbolga_seinnabil = wx.TextCtrl(pnl, value = '', size = (60, 20), pos = (215, 325))