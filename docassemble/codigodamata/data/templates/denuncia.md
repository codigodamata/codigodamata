EXCELENTÍSSIMO SENHOR DOUTOR JUIZ DE DIREITO DA UNIDADE JUDICIAL **${unidade_judicial}** DA COMARCA DE **${comarca}**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

${tipo_procedimento} N. **${simp}**

REQUERIDO:
% for  requerido in requeridos:
**${requerido.name.full()}**,
% endfor

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

${indentation} O **${parte_autora}**, com fundamento nas normas constitucionais e legais vigentes e nos elementos colhidos no  procedimento investigatório em epígrafe, vem à presença de Vossa Excelência oferecer **DENÚNCIA** em desfavor de

&nbsp;

&nbsp;

% for  requerido in requeridos:
> **${requerido.name.full()}**, ${requerido.qualificacao}
  ${"\n"}
% endfor

&nbsp;

&nbsp;

pela prática, em tese, dos seguintes fatos delituosos:

&nbsp;
&nbsp;

% for  fato in fatos:
**DA INFRAÇÃO PENAL PREVISTA NO ${fato.fundamento_normativo.upper()}**

${indentation} ${fato.descricao_fato_tipico_1a_parte} o requerido **${todos_requeridos}** ${fato.descricao_fato_tipico_2a_parte}.

&nbsp;
&nbsp;

${indentation} ${fato.noticia_crime}

&nbsp;
&nbsp;

${indentation} ${fato.diligencia_realizada}

&nbsp;
&nbsp;

${indentation} ${fato.paragrafo_materialidade}

&nbsp;
&nbsp;

${indentation} ${fato.representacao}

&nbsp;
&nbsp;

% endfor



${indentation} Ante o exposto, o **${parte_autora}**, por seu promotor de Justiça signatário, **DENUNCIA** 
% for  requerido in requeridos:
  **${" " + requerido.name.full()}**,
% endfor
como incurso nas sanções previstas no
% for  fato in fatos:
  **${" " + fato.fundamento_normativo}**,
% endfor
requerendo que, recebida e autuada esta inicial, seja ele citado para responder à acusação, e, após a formação da culpa, com observância do contraditório e da ampla defesa, seja prolatada sentença penal condenatória.

&nbsp;
&nbsp;

${indentation} ${cidade}, ${data_hoje}.


&nbsp;
&nbsp;

${indentation} **${subscritor}**

${indentation} ${cargo_subscritor}

&nbsp;

&nbsp;

&nbsp;

&nbsp;

% if testemunhas != None:
**ROL DE TESTEMUNHAS**

${testemunhas}
% endif