import seaborn.objects as so
from gapminder import gapminder


def plot():
    figura = (
        so.Plot(
            data=gapminder[gapminder.continent =="Americas"], 
            x="year", 
            y="gdpPerCap"
        )
        .add(so.Lines(color="#bbca"),group="country")
        .add(so.Line(),so.PolyFit(1))
        .label(
            title="PBI per cápita en los paises americanos",
            x="Año",
            y="PBI per cápita"
        )
    )
    return dict(
        descripcion="PBI per cápita estimado en América",
        autor="Fausto Martínez",
        figura=figura,
    )