import cgpy.colors as cc
import cgpy.devices as cd
import cgpy.universes as cu


def main() -> None:

    poly = [
        cu.Point2D(-9, -8),
        cu.Point2D(-7, -3),
        cu.Point2D(-4, -4),
        cu.Point2D(-3, -6),
        cu.Point2D(-6, -9),
    ]
    win = cu.Window(
        lower_left=cu.Point2D(-10, -10),
        upper_right=cu.Point2D(0, 0),
    )

    dev = cd.Device(
        num_rows=500,
        num_columns=500,
    )

    port = cd.Viewport(
        lower_left=cd.DevicePoint(0, 0),
        num_rows=dev.num_rows,
        num_columns=dev.num_columns,
        device=dev,
    )

    center = cd.DevicePoint(x=dev.num_columns // 2, y=dev.num_rows // 2)

    for x in range(dev.num_columns):
        cd.draw_line_bresenham(
            pt0=center,
            pt1=cd.DevicePoint(x, 0),
            color_id=cc.ColorId(1),
            port=port,
        )
        cd.draw_line_bresenham(
            pt0=center,
            pt1=cd.DevicePoint(x, dev.num_rows - 1),
            color_id=cc.ColorId(1),
            port=port,
        )

    for y in range(dev.num_rows):
        cd.draw_line_bresenham(
            pt0=center,
            pt1=cd.DevicePoint(0, y),
            color_id=cc.ColorId(1),
            port=port,
        )
        cd.draw_line_bresenham(
            pt0=center,
            pt1=cd.DevicePoint(dev.num_rows - 1, y),
            color_id=cc.ColorId(1),
            port=port,
        )

    palette = [cc.Color(0, 0, 0), cc.Color(1, 1, 1)]
    # cd.device_to_png(dev, palette, pathlib.Path("/dev/shm/eita.png"))
    cd.show_device(dev, palette, close_after_milliseconds=50000)


if __name__ == "__main__":
    main()
