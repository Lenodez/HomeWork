def chislo_v_stepen(chislo, step):
    if step == -1:
        return 1/chislo
    stepen_m_odin = chislo_v_stepen(chislo=chislo, step=step + 1)
    return (1/chislo) * stepen_m_odin


print(chislo_v_stepen(5, -3))
