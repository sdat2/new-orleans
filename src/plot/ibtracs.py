"""IBTRACS plotting."""
import os
import matplotlib.axes
import matplotlib.pyplot as plt
import xarray as xr
from sithom.misc import in_notebook
from sithom.time import timeit
from sithom.plot import plot_defaults
from src.constants import FIGURE_PATH, GOM_BBOX, NO_BBOX
from src.data_loading.ibtracs import na_tcs, gom_tcs
from src.plot.map import map_axes


def plot_storm(
    ax: matplotlib.axes.Axes,
    ds: xr.Dataset,
    var: str = "storm_speed",
    storm_num: int = 0,
    cmap="viridis",
    scatter_size: float = 1.6,
) -> None:
    """
    Plot storm.

    Args:
        ds (xr.Dataset): IBTRACS dataset.
        var (str, optional): Variable to plot. Defaults to "storm_speed".
        storm_num (int, optional): Which storm to plot. Defaults to 0.
        cmap (str, optional): Which cmap to use. Defaults to "viridis".
    """
    ax.plot(
        ds[var].isel(storm=storm_num)["lon"].values,
        ds[var].isel(storm=storm_num)["lat"].values,
        color="black",
        linewidth=0.1,
        alpha=0.5,
    )
    ax.scatter(
        ds[var].isel(storm=storm_num)["lon"].values,
        ds[var].isel(storm=storm_num)["lat"].values,
        c=ds[var].isel(storm=storm_num).values,
        marker=".",
        s=scatter_size,
        cmap=cmap,
    )


@timeit
def plot_all_storms(
    ds: xr.Dataset, var="storm_speed", cmap="viridis", scatter_size: float = 1.6
) -> None:
    """
    Plot all the storms in an IBTRACS dataset.

    Args:
        ds (xr.Dataset): IBTRACS dataset.
        var (str, optional): Variable to plot. Defaults to "storm_speed".
        cmap (str, optional): Colormap. Defaults to "viridis".
    """
    ax = map_axes()
    for num in range(0, ds.storm.shape[0]):
        plot_storm(ds, var=var, storm_num=num, cmap=cmap, scatter_size=scatter_size)

    plt.ylabel(r"Latitude [$^{\circ}$N]")
    plt.xlabel(r"Longitude [$^{\circ}$E]")
    plt.colorbar(label=var + " [" + ds[var].attrs["units"] + "]")


@timeit
def plot_na_tcs(var="storm_speed") -> None:
    """
    Plot NA Tropical Cyclones.
    """
    # plot_defaults()
    plot_all_storms(na_tcs(), var=var)
    plt.savefig(os.path.join(FIGURE_PATH, "na_tc_speed.png"))
    if not in_notebook:
        plt.clf()


@timeit
def plot_gom_tcs(var="storm_speed") -> None:
    """
    Plot GOM Tropical Cyclones.
    """
    # plot_defaults()
    plot_all_storms(gom_tcs(), var=var)
    plt.savefig(os.path.join(FIGURE_PATH, "gom_tc_speed.png"))
    if not in_notebook:
        plt.clf()


if __name__ == "__main__":
    # python src/plot/ibtracs.py
    plot_defaults()
    plot_na_tcs()
    plot_gom_tcs()
    print(GOM_BBOX)
    print(NO_BBOX)
