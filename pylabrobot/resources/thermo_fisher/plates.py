"""Thermo Fisher Scientific  Inc. (and all its brand) plates"""

from pylabrobot.resources.well import (
  Well,
  WellBottomType,
  CrossSectionType,
)
from pylabrobot.resources.utils import create_ordered_items_2d
from pylabrobot.resources.plate import Lid, Plate

from pylabrobot.resources.height_volume_functions import (
  calculate_liquid_height_in_container_2segments_square_ubottom,
  calculate_liquid_volume_container_2segments_square_ubottom,
)


# Please conform with the 'manufacturer-first, then brands' naming principle:

# Thermo Fisher Scientific Inc. (TFS, aka "Thermo")
# ├── Applied Biosystems (AB; brand)
# │   └── MicroAmp
# │      └── EnduraPlate
# ├── Fisher Scientific (FS; brand)
# ├── Invitrogen (INV; brand)
# ├── Ion Torrent (IT; brand)
# ├── Gibco (GIB; brand)
# ├── Thermo Scientific (TS; brand)
# │   ├── Nalgene
# │   ├── Nunc
# │   └── Pierce
# ├── Unity Lab Services (brand, services)
# ├── Patheon (brand, services)
# └── PPD (brand, services)


# # # # # # # # # # Thermo_TS_96_wellplate_1200ul_Rb # # # # # # # # # #


def _compute_volume_from_height_Thermo_TS_96_wellplate_1200ul_Rb(
  h: float,
):
  if h > 20.5:
    raise ValueError(f"Height {h} is too large for" + "Thermo_TS_96_wellplate_1200ul_Rb")
  return calculate_liquid_volume_container_2segments_square_ubottom(
    x=8.15, h_cuboid=16.45, liquid_height=h
  )


def _compute_height_from_volume_Thermo_TS_96_wellplate_1200ul_Rb(
  liquid_volume: float,
):
  if liquid_volume > 1260:  # 5% tolerance
    raise ValueError(
      f"Volume {liquid_volume} is too large for" + "Thermo_TS_96_wellplate_1200ul_Rb"
    )
  return round(
    calculate_liquid_height_in_container_2segments_square_ubottom(
      x=8.15, h_cuboid=16.45, liquid_volume=liquid_volume
    ),
    3,
  )


def Thermo_TS_96_wellplate_1200ul_Rb_Lid(name: str) -> Lid:
  raise NotImplementedError("This lid is not currently defined.")
  # See https://github.com/PyLabRobot/pylabrobot/pull/161.
  # return Lid(
  #   name=name,
  #   size_x=127.76,
  #   size_y=85.48,
  #   size_z=5,
  #   nesting_z_height=None, # measure overlap between lid and plate
  #   model="ThermoScientific_96_DWP_1200ul_Rd_Lid",
  # )


def ThermoScientific_96_DWP_1200ul_Rd(name: str, with_lid: bool = False) -> Plate:
  raise NotImplementedError(
    "This function is deprecated and will be removed in a future version."
    " Use 'Thermo_TS_96_wellplate_1200ul_Rb' instead."
  )


def ThermoScientific_96_wellplate_1200ul_Rd(name: str, with_lid: bool = False) -> Plate:
  raise NotImplementedError(
    "This function is deprecated and will be removed in a future version."
    " Use 'Thermo_TS_96_wellplate_1200ul_Rb' instead."
  )


def Thermo_TS_96_wellplate_1200ul_Rb(name: str, with_lid: bool = False) -> Plate:
  """Thermo Fisher Scientific/Fisher Scientific cat. no.: AB1127/10243223.
  - Material: Polypropylene (AB-1068, polystyrene).
  - Brand: Thermo Scientific.
  - Sterilization compatibility: Autoclaving (15 minutes at 121°C) or
    Gamma Irradiation.
  - Chemical resistance: to DMSO (100%); Ethanol (100%); Isopropanol (100%).
  - Round well shape designed for optimal sample recovery or square shape to
    maximize sample volume within ANSI footprint design.
  - Each well has an independent sealing rim to prevent cross-contamination
  - U-bottomed wells ideally suited for sample resuspension.
  - Sealing options: Adhesive Seals, Heat Seals, Storage Plate Caps and Cap
    Strips, and Storage Plate Sealing Mats.
  - Cleanliness: 10243223/AB1127: Cleanroom manufacture.
  - ANSI/SLAS-format for compatibility with automated systems.
  """
  return Plate(
    name=name,
    size_x=127.76,
    size_y=85.48,
    size_z=24.0,
    lid=Thermo_TS_96_wellplate_1200ul_Rb_Lid(name + "_lid") if with_lid else None,
    model="Thermo_TS_96_wellplate_1200ul_Rb",
    ordered_items=create_ordered_items_2d(
      Well,
      num_items_x=12,
      num_items_y=8,
      dx=10.0,
      dy=7.3,
      dz=2.5,  # 2.5. https://github.com/PyLabRobot/pylabrobot/pull/183
      item_dx=9,
      item_dy=9,
      size_x=8.3,
      size_y=8.3,
      size_z=20.5,
      bottom_type=WellBottomType.U,
      material_z_thickness=1.15,
      cross_section_type=CrossSectionType.RECTANGLE,
      compute_volume_from_height=(_compute_volume_from_height_Thermo_TS_96_wellplate_1200ul_Rb),
      compute_height_from_volume=(_compute_height_from_volume_Thermo_TS_96_wellplate_1200ul_Rb),
    ),
  )


def Thermo_TS_96_wellplate_1200ul_Rb_L(name: str, with_lid: bool = False) -> Plate:
  return Thermo_TS_96_wellplate_1200ul_Rb(name=name, with_lid=with_lid)


def Thermo_TS_96_wellplate_1200ul_Rb_P(name: str, with_lid: bool = False) -> Plate:
  return Thermo_TS_96_wellplate_1200ul_Rb(name=name, with_lid=with_lid).rotated(90)


# # # # # # # # # # Thermo_AB_96_wellplate_300ul_Vb_EnduraPlate # # # # # # # # # #


def _compute_volume_from_height_Thermo_AB_96_wellplate_300ul_Vb_EnduraPlate(
  h: float,
):
  if h > 21.1:
    raise ValueError(f"Height {h} is too large for" + "ThermoScientific_96_wellplate_1200ul_Rd")
  return max(
    0.9617 + 10.2590 * h - 1.3069 * h**2 + 0.26799 * h**3 - 0.01003 * h**4,
    0,
  )


def _compute_height_from_volume_Thermo_AB_96_wellplate_300ul_Vb_EnduraPlate(
  liquid_volume: float,
):
  if liquid_volume > 315:  # 5% tolerance
    raise ValueError(
      f"Volume {liquid_volume} is too large for" + "ThermoScientific_96_wellplate_1200ul_Rd"
    )
  return max(
    -0.1823
    + 0.1327 * liquid_volume
    - 0.000637 * liquid_volume**2
    + 1.6577e-6 * liquid_volume**3
    - 1.1487e-9 * liquid_volume**4,
    0,
  )


# results_measurement_fitting_dict = {
#     "Volume (ul)": [0, 4, 8, 20, 70, 120, 170, 220, 260],
#     "Observed Height (mm)": [0, 0.17, 0.77, 2.27, 6.57, 9.17, 11.17, 13.17, 15.17],
#     "Predicted Height (mm)": [0, 0.338, 0.839, 2.230, 6.526, 9.195, 11.152, 13.141, 15.145],
#     "Relative Deviation (%)": [0, 99.07, 9.01, -1.76, -0.66, 0.27, -0.16, -0.22, -0.17]
# }


def Thermo_AB_96_wellplate_300ul_Vb_EnduraPlate_Lid(name: str) -> Lid:
  raise NotImplementedError("This lid is not currently defined.")
  # See https://github.com/PyLabRobot/pylabrobot/pull/161.
  # return Lid(
  #   name=name,
  #   size_x=127.76,
  #   size_y=85.48,
  #   size_z=5,
  #   nesting_z_height=None, # measure overlap between lid and plate
  #   model="Thermo_AB_96_wellplate_300ul_Vb_EnduraPlate_Lid",
  # )


def Thermo_AB_96_wellplate_300ul_Vb_EnduraPlate(name: str, with_lid: bool = False) -> Plate:
  """Thermo Fisher Scientific/Fisher Scientific cat. no.: 4483354/15273005 (= with barcode)
  - Part no.: 16698853 (FS) (= **without** barcode).
  - See `./engineering_diagrams/` directory for more part numbers (different colours).
  - Material: Polycarbonate, Polypropylene.
  - Sterilization compatibility: ?
  - Chemical resistance: ?
  - Thermal resistance: ?
  - Cleanliness: 'Certified DNA-, RNAse-, and PCR inhibitor-free with in-process sampling tests'.
  - ANSI/SLAS-format for compatibility with automated systems.
  - optimal pickup_distance_from_top=4 mm.
  - total_volume = 300 ul.
  - working_volume = 200 ul (recommended by manufacturer).
  """
  return Plate(
    name=name,
    size_x=127.76,
    size_y=85.48,
    size_z=20.1 + 1.6 - 0.5,  # cavity_depth + material_z_thickness - well_extruding_over_plate
    lid=Thermo_AB_96_wellplate_300ul_Vb_EnduraPlate_Lid(name + "_lid") if with_lid else None,
    model="Thermo_AB_96_wellplate_300ul_Vb_EnduraPlate",
    plate_type="semi-skirted",
    ordered_items=create_ordered_items_2d(
      Well,
      num_items_x=12,
      num_items_y=8,
      dx=11.63,
      dy=9.95,
      dz=0.0,  # check that plate is semi-skirted
      item_dx=9,
      item_dy=9,
      size_x=5.49,
      size_y=5.49,
      size_z=20.1,
      bottom_type=WellBottomType.V,
      material_z_thickness=1.6,
      cross_section_type=CrossSectionType.CIRCLE,
      compute_volume_from_height=(
        _compute_volume_from_height_Thermo_AB_96_wellplate_300ul_Vb_EnduraPlate
      ),
      compute_height_from_volume=(
        _compute_height_from_volume_Thermo_AB_96_wellplate_300ul_Vb_EnduraPlate
      ),
    ),
  )


def Thermo_AB_96_wellplate_300ul_Vb_EnduraPlate_L(name: str, with_lid: bool = False) -> Plate:
  return Thermo_AB_96_wellplate_300ul_Vb_EnduraPlate(name=name, with_lid=with_lid)


def Thermo_AB_96_wellplate_300ul_Vb_EnduraPlate_P(name: str, with_lid: bool = False) -> Plate:
  return Thermo_AB_96_wellplate_300ul_Vb_EnduraPlate(name=name, with_lid=with_lid).rotated(90)



# # # # # # # # # # Thermo_FS_96_wellplate_200_Vb_semi-skirted # # # # # # # # # #
# Pub No. MAN0014411


def _compute_volume_from_height_Thermo_FS_96_wellplate_300ul_Vb_semi_skirted(
    h: float,
):
  raise NotImplementedError("This function is not implemented yet")


def _compute_height_from_volume_Thermo_FS_96_wellplate_300ul_Vb_semi_skirted(
    liquid_volume: float,
):
  raise NotImplementedError("This function is not implemented yet")


def Thermo_FS_96_wellplate_300ul_Vb_semi_skirted_Lid(name: str) -> Lid:
  raise NotImplementedError("This lid is not currently defined.")




def Thermo_FS_96_wellplate_300ul_Vb_semi_skirted(name: str, with_lid: bool = False) -> Plate:
  """Thermo Fisher Scientific/Fisher Scientific cat. no.: AB0990.
  - See `./engineering_diagrams/` directory for more part numbers.
  - Material: Polypropylene.
  - Sterilization compatibility: ?
  - Chemical resistance: ?
  - Thermal resistance: ?
  - Cleanliness: 'Certified RNase/DNase-free'.
  - Format: ??? (Maybe: ANSI/SLAS-format for compatibility with automated systems.)
  - ??? (Maybe: optimal pickup_distance_from_top=4 mm.)
  - total_volume = 300 ul.
  - working_volume = 200 ul (recommended by manufacturer).
  - Cut corner: H1.
  - Can be cut into 24 and 48 well sections.
  """
  return Plate(
    name=name,
    size_x=120.0,
    size_y=80.0,
    size_z=19.5 + 0.6 - 0.5,  # cavity_depth(19.5) + material_z_thickness(0.6) - well_extruding_over_plate(0.5)
    lid=Thermo_FS_96_wellplate_300ul_Vb_semi_skirted_Lid(name + "_lid") if with_lid else None,
    model="Thermo_FS_96_wellplate_300ul_Vb_semi_skirted",
    plate_type="semi-skirted",
    ordered_items=create_ordered_items_2d(
      Well,
      num_items_x=12,
      num_items_y=8,
      dx=11.63,
      dy=9.95,
      dz=0.0,  # check that plate is semi-skirted
      item_dx=9,
      item_dy=9,
      size_x=5.49,
      size_y=5.49,
      size_z=20.1,
      bottom_type=WellBottomType.V,
      material_z_thickness=1.6,
      cross_section_type=CrossSectionType.CIRCLE,
      compute_volume_from_height=(
        _compute_volume_from_height_Thermo_FS_96_wellplate_300ul_Vb_semi_skirted
      ),
      compute_height_from_volume=(
        _compute_height_from_volume_Thermo_FS_96_wellplate_300ul_Vb_semi_skirted
      ),
    ),
  )
