

DATA_PATH = '/home/investigacion/Dropbox/Brain/UAM/Cursos/SyMP/db/'
DATA_PATH = '/home/investigacion/Dropbox/Brain/UAM/Cursos/SyS-PIB/db/'

def get_data(fdata):
    db = pd.read_excel(DATA_PATH+fdata,
                          sheet_name=None)
    return db

def to_latex(df):
    tab = df.to_latex(index=False)
    tab = tab.replace('\n\\toprule','')
    tab = tab.replace('\n\\midrule','')
    tab = tab.replace('\n\\bottomrule','')
    tab = tab.replace('\n','\n\t')
    
    return tab[:-2]

def cuenta_sesiones(df):
    Sesiones = []
    #pd.to_datetime(df['fecha'],format='%d/%m/%y')
    for g,gvalues in df.groupby( pd.Grouper(key='fecha', axis=0, freq='M') ):
        sesiones = {}
        query    = gvalues.query("tipo=='laborable' & `tipo sesion`=='teoria'")
        sesiones['mes']             = g.month_name()
        sesiones['sesiones teoria'] = query.shape[0]
        
        query = gvalues.query("tipo=='laborable' & `tipo sesion`=='laboratorio'")
        sesiones['sesiones lab'] = query.shape[0]
        
        Sesiones.append(sesiones)
    
    tab =  to_latex(pd.DataFrame(Sesiones))
    return tab

def cuenta_descansos(df):
    query = df.query("tipo=='descanso' & not `tipo sesion`.isnull()")
    query = query.drop(columns='tipo')
    
    tab = to_latex(query)
    return tab

def cuadro_sesiones(tab):
    header = """
    \\begin{tabular}{lcc}
    	  \\multicolumn{1}{c}{\\bf Mes}
	    & \\multicolumn{2}{c}{\\bf Sesiones}\\\\
	  \\cline{2-3}
	  {}
	    & \\multicolumn{1}{c}{\\bf Teoría}
	    & \\multicolumn{1}{c}{\\bf Laboratorio}\\\\
    """
    tab = tab.replace('\\begin{tabular}{lrr}',header)
    
    return tab

def cuadro_descansos(tab):
    header = """{cllc}
    	     {\\bf Fecha} 
    	       &\\multicolumn{1}{c}{\\bf Día}
    	       &\\multicolumn{1}{c}{\\bf Tipo Sesión}
    	       &\\multicolumn{1}{c}{\\bf Semana }\\\\
    """
    tab = tab.replace('{lllr}',header)
    
    return tab

def cuadro_resumen_sesiones(df,tab_sesiones,tab_descanso):
    sesiones_teo = df.query("`tipo sesion`=='teoria'"     ).shape[0]
    sesiones_lab = df.query("`tipo sesion`=='laboratorio'").shape[0]
    
    msg  = "Sesiones de teoría: %d\n"              %sesiones_teo
    msg += "\\rowcolors{4}{ForestGreen!2}{ForestGreen!20}\n"
    msg += "\\begin{center}\n%s\n\\end{center}\n\n"%tab_sesiones
    msg += "Días de descanso: %d\n"         %sesiones_lab
    msg += "\\rowcolors{2}{ForestGreen!2}{ForestGreen!20}\n"
    msg += "\\begin{center}\n%s\n\\end{center}"    %tab_descanso
    clip.copy(msg)
    print("\n\n\nSe copió al porta papeles el cuadro de resumen de sesiones\n\n\nPresiona una tecla para continuar")
    pdb.set_trace()

def main():
    data = get_data('planeacion.ods')
    
    df           = data['sesiones'].dropna()
    tab_sesiones = cuenta_sesiones(df)
    tab_sesiones = cuadro_sesiones(tab_sesiones)
    
    df           = data['sesiones']
    tab_descanso = cuenta_descansos(df)
    tab_descanso = cuadro_descansos(tab_descanso)
    
    cuadro_resumen_sesiones(df,tab_sesiones,tab_descanso)
    pdb.set_trace()
    
   