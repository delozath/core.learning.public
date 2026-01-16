
from typing import Self

from omegaconf import DictConfig

import pandas as pd


class Calendario:
    DIAS  = [
        'lunes',
        'martes',
        'miércoles',
        'jueves',
        'viernes'
    ]

    def trimestre(
        self,
        inicio: str,
        fin: str,
        dictionary: dict[dict,
        str],
        uam_offset: int
     ) -> Self:
        """
        Genera el calendario del trimestre académico de la UAM.
        
        Arguments
        ----------
        inicio : str
            Fecha de inicio del trimestre en formato 'YYYY.MM.DD'.
        fin : str
            Fecha de fin del trimestre en formato 'YYYY.MM.DD'.
        dictionary : dict[dict, str]
            Diccionario de traducción para días y meses.
        uam_offset : int
            Desfase en semanas respecto al calendario nominal.
        
        Returns
        -------
        Self
            Instancia de la clase Calendario con el trimestre generado.
        """
        fechas = pd.Series(
            pd.date_range(
                start=inicio,
                end=fin,
                freq='d'
            ),
            name='fecha'
         )
        trim = self._traduce(fechas, dictionary)
        trim = self._compute_uam_weeks(trim, uam_offset)
        
        trim = trim.query("dia.isin(@self.DIAS)").copy()
        trim['tipo_sesion'] = None
        self.trim = trim
        return self
    
    def sesiones(self, calendario: pd.DataFrame, sesiones: DictConfig) -> pd.DataFrame:
        """
        Asigna los tipos de sesión al calendario del trimestre.
        - Genera diccionario dia:lugar
        - Reemplaza dias por lugar de la sesión
        - Asigna tipo de sesión para despligue
        
        Arguments
        ----------
        calendario : pd.DataFrame
            DataFrame con el calendario del trimestre.
        sesiones : DictConfig
            Configuración de las sesiones con días, lugar y tipos.
        
        Returns
        -------
        pd.DataFrame
            DataFrame del calendario con tipos de sesión asignados.
        """
        calendario['lugar'] = calendario['dia'].copy()
        for ses in sesiones.sesiones:
            curso_info = [*ses.values()][0]
            dias_map = dict(zip(self.DIAS, (curso_info.dias)))
            dias = {d:s for d, s in dias_map.items() if s!=0}

            calendario = calendario.replace({'lugar': dias})
            calendario.loc[calendario.dia.isin(dias), 'tipo_sesion'] = curso_info.name
        
        return calendario.query("tipo_sesion.notnull()").copy()

    def remover_eventos(self, calendario: pd.DataFrame, evt_dict: DictConfig) -> pd.DataFrame:
        """
        Remueve los eventos especiales del calendario del trimestre.

        Arguments
        ----------
        calendario : pd.DataFrame
            DataFrame con el calendario del trimestre.
        evt_dict : DictConfig
            Configuración de los tipos de eventos y sus fechas.
        
        Returns
        -------
        pd.DataFrame
            DataFrame del calendario con eventos removidos.
        
        """
        trim = calendario.set_index('fecha')
        for evt, dt in evt_dict.eventos.items():
            mask = pd.to_datetime(dt).intersection(trim.index)
            if mask.empty:
                print(f"\nNingún evento tipo '{evt}' en el trimestre")
            else:
                trim.loc[mask, 'tipo_sesion'] = None
        return trim.query("tipo_sesion.notnull()").copy()
    
    def _traduce(self, fechas: pd.Series, dictionary: dict[dict, str]) -> pd.DataFrame:
        dias = fechas.dt.day_name().replace(dictionary.dias)
        meses = fechas.dt.month_name().replace(dictionary.meses)
        dias.name = 'dia'
        meses.name = 'mes'

        calendario = pd.concat([fechas, dias, meses], axis=1)
        return calendario
    
    def _compute_uam_weeks(self, calendario: pd.DataFrame, uam_offset: int) -> pd.DataFrame:
        semana_uam = calendario.fecha.dt.isocalendar().week.astype('int') -  uam_offset
        semana_uam.name = 'semana_uam'
        calendario = pd.concat([calendario, semana_uam], axis=1)
        return calendario
