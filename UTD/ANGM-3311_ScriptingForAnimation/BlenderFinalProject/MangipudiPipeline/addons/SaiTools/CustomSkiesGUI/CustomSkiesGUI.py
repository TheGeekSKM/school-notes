from PySide2 import QtWidgets
from . import CustomSkiesFunctions

class SkiesGUI(QtWidgets.QWidget):
    def __init__(self, parent=None, *args, **kwargs):
        super(SkiesGUI, self).__init__(parent=parent)
        self.setup_ui()
    
    def setup_ui(self):
        self.setWindowTitle("Custom Skies GUI")
        self.setGeometry(100, 100, 800, 600)
        
        self.create_widgets()
        self.create_layouts()
        self.create_signals()
        
        self.show()
    
    
    #region Widget Definitions
    def define_complete_random_sky(self):
        self.complete_random_label = QtWidgets.QLabel("Complete Random Sky")
        self.complete_random_description = QtWidgets.QLabel("This button will set up a completely random sky and will not follow any rules.")
        self.complete_random_description.wordWrap = True
        self.complete_random_button = QtWidgets.QPushButton("Random Sky")
        self.complete_random_button.setToolTip("Set up a completely random sky")
    
    def define_preexisting_sky(self):
        self.preexisting_sky_title_label = QtWidgets.QLabel("Pre-existing Sky")
        self.preexisting_sky_label = QtWidgets.QLabel("Click on any of the buttons below to set up a pre-existing sky.")
        self.moon_atmosphere_button = QtWidgets.QPushButton("Moon Atmosphere")
        self.dusty_atmosphere_button = QtWidgets.QPushButton("Dusty Atmosphere")
        self.soft_sunset_button = QtWidgets.QPushButton("Soft Sunset")
        self.harsh_sunset_button = QtWidgets.QPushButton("Harsh Sunset")
        self.cloudy_day_button = QtWidgets.QPushButton("Cloudy/Overcast Day")
        self.normal_day_button = QtWidgets.QPushButton("Normal Daylight")
        
    def define_sky_settings_title(self):
        self.sky_settings_label = QtWidgets.QLabel("Sky Settings")
        self.sky_settings_description = QtWidgets.QLabel("Adjust the values below to fine-tune the sky. Press the 'Update Sky' button to apply the changes.")
        self.sky_settings_description.wordWrap = True
        
    def define_sky_settings_sun_rotation(self):
        self.sun_rotation_label = QtWidgets.QLabel("Sun Rotation (degrees)")
        self.sun_rotation_spin_box = QtWidgets.QSpinBox()
        self.sun_rotation_spin_box.setValue(0)
        self.sun_rotation_spin_box.setRange(0, 360)
        
    def define_sky_settings_sun_intensity(self):
        self.sun_intensity_label = QtWidgets.QLabel("Sun Intensity")
        self.sun_intensity_spin_box = QtWidgets.QSpinBox()
        self.sun_intensity_spin_box.setRange(0, 5)
        self.sun_intensity_spin_box.setValue(2)
        
    def define_sky_settings_sun_elevation(self):
        self.sun_elevation_label = QtWidgets.QLabel("Sun Elevation (degrees)")
        self.sun_elevation_spin_box = QtWidgets.QSpinBox()
        self.sun_elevation_spin_box.setRange(0, 90)
        self.sun_elevation_spin_box.setValue(45)
    
    def define_sky_settings_altitude(self):
        self.altitude_label = QtWidgets.QLabel("Altitude (degrees)")
        self.altitude_spin_box = QtWidgets.QSpinBox()
        self.altitude_spin_box.setRange(0, 90)
        self.altitude_spin_box.setValue(45)
    
    def define_sky_settings_air_density(self):
        self.air_density_label = QtWidgets.QLabel("Air Density")
        self.air_density_spin_box = QtWidgets.QSpinBox()
        self.air_density_spin_box.setRange(1, 10)
        self.air_density_spin_box.setValue(5)
        
    def define_sky_settings_dust_density(self):
        self.dust_density_label = QtWidgets.QLabel("Dust Density")
        self.dust_density_spin_box = QtWidgets.QSpinBox()
        self.dust_density_spin_box.setRange(1, 10)
        self.dust_density_spin_box.setValue(5)
    
    def define_sky_settings_ozone_density(self):
        self.ozone_density_label = QtWidgets.QLabel("Ozone Density")
        self.ozone_density_spin_box = QtWidgets.QSpinBox()
        self.ozone_density_spin_box.setRange(1, 10)
        self.ozone_density_spin_box.setValue(5)
    
    def define_sky_settings_sun_size(self):
        self.sun_size_label = QtWidgets.QLabel("Sun Size (degrees)")
        self.sun_size_spin_box = QtWidgets.QSpinBox()
        self.sun_size_spin_box.setRange(0, 90)
        self.sun_size_spin_box.setValue(45)
    
    def define_sky_settings_sky_color(self):
        self.sky_color_label = QtWidgets.QLabel("Sky Color")
        self.sky_color_x_spin_box = QtWidgets.QDoubleSpinBox()
        self.sky_color_x_spin_box.setRange(0.0, 1.0)
        self.sky_color_x_spin_box.setValue(0.5)
        
        self.sky_color_y_spin_box = QtWidgets.QDoubleSpinBox()
        self.sky_color_y_spin_box.setRange(0.0, 1.0)
        self.sky_color_y_spin_box.setValue(0.5)
        
        self.sky_color_z_spin_box = QtWidgets.QDoubleSpinBox()
        self.sky_color_z_spin_box.setRange(0.0, 1.0)
        self.sky_color_z_spin_box.setValue(0.5)
        
    def define_sky_settings_sky_color_prevalence(self):
        self.mix_factor_label = QtWidgets.QLabel("Sky Color Prevalence")
        self.mix_factor_spin_box = QtWidgets.QDoubleSpinBox()
        self.mix_factor_spin_box.setRange(0.1, 0.9)
        self.mix_factor_spin_box.setValue(0.5)
        
    def define_sky_settings_cloud_size(self):
        self.cloud_size_label = QtWidgets.QLabel("Cloud Size")
        self.cloud_size_spin_box = QtWidgets.QSpinBox()
        self.cloud_size_spin_box.setRange(1, 5)
        self.cloud_size_spin_box.setValue(3)
    
    def define_sky_settings_cloud_vector(self):
        self.cloud_vector_label = QtWidgets.QLabel("Cloud Vector")
        self.cloud_vector_x_spin_box = QtWidgets.QDoubleSpinBox()
        self.cloud_vector_x_spin_box.setRange(0.0, 1.0)
        self.cloud_vector_x_spin_box.setValue(0.5)
        
        self.cloud_vector_y_spin_box = QtWidgets.QDoubleSpinBox()
        self.cloud_vector_y_spin_box.setRange(0.0, 1.0)
        self.cloud_vector_y_spin_box.setValue(0.5)
        
        self.cloud_vector_z_spin_box = QtWidgets.QDoubleSpinBox()
        self.cloud_vector_z_spin_box.setRange(0.0, 1.0)
        self.cloud_vector_z_spin_box.setValue(0.5)
        
    def define_sky_settings_cloud_opacity(self):
        self.cloud_opacity_label = QtWidgets.QLabel("Cloud Opacity")
        self.cloud_opacity_spin_box = QtWidgets.QDoubleSpinBox()
        self.cloud_opacity_spin_box.setRange(0.1, 0.9)
        self.cloud_opacity_spin_box.setValue(0.5)
    
    def define_sky_settings_cloud_intensity(self):
        self.cloud_intensity_label = QtWidgets.QLabel("Cloud Intensity")
        self.cloud_intensity_spin_box = QtWidgets.QSpinBox()
        self.cloud_intensity_spin_box.setRange(1, 5)
        self.cloud_intensity_spin_box.setValue(3)
        
    def define_sky_settings_cloud_color(self):
        self.cloud_color_label = QtWidgets.QLabel("Cloud Color")
        self.cloud_color_x_spin_box = QtWidgets.QDoubleSpinBox()
        self.cloud_color_x_spin_box.setRange(0.0, 1.0)
        self.cloud_color_x_spin_box.setValue(0.5)
        
        self.cloud_color_y_spin_box = QtWidgets.QDoubleSpinBox()
        self.cloud_color_y_spin_box.setRange(0.0, 1.0)
        self.cloud_color_y_spin_box.setValue(0.5)
        
        self.cloud_color_z_spin_box = QtWidgets.QDoubleSpinBox()
        self.cloud_color_z_spin_box.setRange(0.0, 1.0)
        self.cloud_color_z_spin_box.setValue(0.5)
        
    def define_sun_settings(self):
        self.define_sky_settings_sun_rotation()
        self.define_sky_settings_sun_intensity()
        self.define_sky_settings_sun_elevation()
        self.define_sky_settings_sun_size()
        
    def define_sky_densities(self):
        self.define_sky_settings_altitude()
        self.define_sky_settings_air_density()
        self.define_sky_settings_dust_density()
        self.define_sky_settings_ozone_density()
        
    def define_sky_values(self):
        self.define_sky_settings_sky_color()
        self.define_sky_settings_sky_color_prevalence()
        
    def define_cloud_values(self):
        self.define_sky_settings_cloud_size()
        self.define_sky_settings_cloud_vector()
        self.define_sky_settings_cloud_opacity()
        self.define_sky_settings_cloud_intensity()
        self.define_sky_settings_cloud_color()
        
    def define_update_sky_button(self):
        self.update_sky_button = QtWidgets.QPushButton("Update Sky")
        self.update_sky_button.setToolTip("Update the sky with the new settings")
    #endregion
    
    def create_widgets(self):
        self.define_complete_random_sky()
        self.define_preexisting_sky()
        self.define_sky_settings_title()
        self.define_sun_settings()
        self.define_sky_densities()
        self.define_sky_values()
        self.define_cloud_values()
        self.define_update_sky_button()
    
    #region Layouts
    def layout_random_sky(self):
        self.random_sky_layout = QtWidgets.QVBoxLayout()
        self.random_sky_layout.addWidget(self.complete_random_label)
        self.random_sky_layout.addWidget(self.complete_random_description)
        self.random_sky_layout.addWidget(self.complete_random_button)
        
    def layout_preexisting_sky(self):
        self.preexisting_sky_layout = QtWidgets.QVBoxLayout()
        self.preexisting_sky_layout.addWidget(self.preexisting_sky_title_label)
        self.preexisting_sky_layout.addWidget(self.preexisting_sky_label)
        self.preexisting_sky_layout.addWidget(self.moon_atmosphere_button)
        self.preexisting_sky_layout.addWidget(self.dusty_atmosphere_button)
        self.preexisting_sky_layout.addWidget(self.soft_sunset_button)
        self.preexisting_sky_layout.addWidget(self.harsh_sunset_button)
        self.preexisting_sky_layout.addWidget(self.cloudy_day_button)
        self.preexisting_sky_layout.addWidget(self.normal_day_button)
        
    def layout_sky_settings_title(self):
        self.sky_settings_title_layout = QtWidgets.QVBoxLayout()
        self.sky_settings_title_layout.addWidget(self.sky_settings_label)
        self.sky_settings_title_layout.addWidget(self.sky_settings_description)
        
    def layout_sky_settings_sun_rotation(self):
        self.sun_rotation_layout = QtWidgets.QHBoxLayout()
        self.sun_rotation_layout.addWidget(self.sun_rotation_label)
        self.sun_rotation_layout.addWidget(self.sun_rotation_spin_box)
        
    def layout_sky_settings_sun_intensity(self):
        self.sun_intensity_layout = QtWidgets.QHBoxLayout()
        self.sun_intensity_layout.addWidget(self.sun_intensity_label)
        self.sun_intensity_layout.addWidget(self.sun_intensity_spin_box)
        
    def layout_sky_settings_sun_elevation(self):
        self.sun_elevation_layout = QtWidgets.QHBoxLayout()
        self.sun_elevation_layout.addWidget(self.sun_elevation_label)
        self.sun_elevation_layout.addWidget(self.sun_elevation_spin_box)
        
    def layout_sky_settings_sun_size(self):
        self.sun_size_layout = QtWidgets.QHBoxLayout()
        self.sun_size_layout.addWidget(self.sun_size_label)
        self.sun_size_layout.addWidget(self.sun_size_spin_box)
        
    def layout_sky_settings_altitude(self):
        self.altitude_layout = QtWidgets.QHBoxLayout()
        self.altitude_layout.addWidget(self.altitude_label)
        self.altitude_layout.addWidget(self.altitude_spin_box)
        
    def layout_sky_settings_air_density(self):
        self.air_density_layout = QtWidgets.QHBoxLayout()
        self.air_density_layout.addWidget(self.air_density_label)
        self.air_density_layout.addWidget(self.air_density_spin_box)
        
    def layout_sky_settings_dust_density(self):
        self.dust_density_layout = QtWidgets.QHBoxLayout()
        self.dust_density_layout.addWidget(self.dust_density_label)
        self.dust_density_layout.addWidget(self.dust_density_spin_box)
    
    def layout_sky_settings_ozone_density(self):
        self.ozone_density_layout = QtWidgets.QHBoxLayout()
        self.ozone_density_layout.addWidget(self.ozone_density_label)
        self.ozone_density_layout.addWidget(self.ozone_density_spin_box)
    
    
    def layout_sky_settings_sky_color(self):
        self.sky_color_layout = QtWidgets.QHBoxLayout()
        self.sky_color_layout.addWidget(self.sky_color_label)
        self.sky_color_layout.addWidget(self.sky_color_x_spin_box)
        self.sky_color_layout.addWidget(self.sky_color_y_spin_box)
        self.sky_color_layout.addWidget(self.sky_color_z_spin_box)
        
    def layout_sky_settings_sky_color_prevalence(self):
        self.mix_factor_layout = QtWidgets.QHBoxLayout()
        self.mix_factor_layout.addWidget(self.mix_factor_label)
        self.mix_factor_layout.addWidget(self.mix_factor_spin_box)
        
    def layout_sky_settings_cloud_size(self):
        self.cloud_size_layout = QtWidgets.QHBoxLayout()
        self.cloud_size_layout.addWidget(self.cloud_size_label)
        self.cloud_size_layout.addWidget(self.cloud_size_spin_box)
        
    def layout_sky_settings_cloud_vector(self):
        self.cloud_vector_layout = QtWidgets.QHBoxLayout()
        self.cloud_vector_layout.addWidget(self.cloud_vector_label)
        self.cloud_vector_layout.addWidget(self.cloud_vector_x_spin_box)
        self.cloud_vector_layout.addWidget(self.cloud_vector_y_spin_box)
        self.cloud_vector_layout.addWidget(self.cloud_vector_z_spin_box)
        
    def layout_sky_settings_cloud_opacity(self):
        self.cloud_opacity_layout = QtWidgets.QHBoxLayout()
        self.cloud_opacity_layout.addWidget(self.cloud_opacity_label)
        self.cloud_opacity_layout.addWidget(self.cloud_opacity_spin_box)
        
    def layout_sky_settings_cloud_intensity(self):
        self.cloud_intensity_layout = QtWidgets.QHBoxLayout()
        self.cloud_intensity_layout.addWidget(self.cloud_intensity_label)
        self.cloud_intensity_layout.addWidget(self.cloud_intensity_spin_box)

    def layout_sky_settings_cloud_color(self):
        self.cloud_color_layout = QtWidgets.QHBoxLayout()
        self.cloud_color_layout.addWidget(self.cloud_color_label)
        self.cloud_color_layout.addWidget(self.cloud_color_x_spin_box)
        self.cloud_color_layout.addWidget(self.cloud_color_y_spin_box)
        self.cloud_color_layout.addWidget(self.cloud_color_z_spin_box)
        
    def layout_update_sky_button(self):
        self.update_sky_layout = QtWidgets.QHBoxLayout()
        self.update_sky_layout.addWidget(self.update_sky_button)
        
    def layout_sky_settings(self):
        self.layout_sky_settings_sun_rotation()
        self.layout_sky_settings_sun_intensity()
        self.layout_sky_settings_sun_elevation()
        self.layout_sky_settings_sun_size()
        self.layout_sky_settings_altitude()
        self.layout_sky_settings_air_density()
        self.layout_sky_settings_dust_density()
        self.layout_sky_settings_ozone_density()
        self.layout_sky_settings_sky_color()
        self.layout_sky_settings_sky_color_prevalence()
        self.layout_sky_settings_cloud_size()
        self.layout_sky_settings_cloud_vector()
        self.layout_sky_settings_cloud_opacity()
        self.layout_sky_settings_cloud_intensity()
        self.layout_sky_settings_cloud_color()
        self.layout_update_sky_button()
    #endregion
        
    def create_layouts(self):
        self.main_layout = QtWidgets.QVBoxLayout()
        self.layout_random_sky()
        
        self.layout_preexisting_sky()
        
        self.layout_sky_settings_title()
        self.layout_sky_settings()
        
        self.main_layout.addLayout(self.random_sky_layout)
        self.main_layout.addLayout(self.preexisting_sky_layout)
        self.main_layout.addLayout(self.sky_settings_title_layout)
        self.main_layout.addLayout(self.sun_rotation_layout)
        self.main_layout.addLayout(self.sun_intensity_layout)
        self.main_layout.addLayout(self.sun_elevation_layout)
        self.main_layout.addLayout(self.sun_size_layout)
        self.main_layout.addLayout(self.altitude_layout)
        self.main_layout.addLayout(self.air_density_layout)
        self.main_layout.addLayout(self.dust_density_layout)
        self.main_layout.addLayout(self.ozone_density_layout)
        self.main_layout.addLayout(self.sky_color_layout)
        self.main_layout.addLayout(self.mix_factor_layout)
        self.main_layout.addLayout(self.cloud_size_layout)
        self.main_layout.addLayout(self.cloud_vector_layout)
        self.main_layout.addLayout(self.cloud_opacity_layout)
        self.main_layout.addLayout(self.cloud_intensity_layout)
        self.main_layout.addLayout(self.cloud_color_layout)
        self.main_layout.addLayout(self.update_sky_layout)
        
        self.setLayout(self.main_layout)
    
    
    def create_signals(self):
        self.complete_random_button.clicked.connect(self.complete_random_sky)
        
        self.moon_atmosphere_button.clicked.connect(self.moon_atmosphere_sky)
        self.dusty_atmosphere_button.clicked.connect(self.dusty_atmosphere_sky)
        self.soft_sunset_button.clicked.connect(self.soft_sunset_sky)
        self.harsh_sunset_button.clicked.connect(self.harsh_sunset_sky)
        self.cloudy_day_button.clicked.connect(self.cloudy_day_sky)
        self.normal_day_button.clicked.connect(self.normal_day_sky)
        
        self.update_sky_button.clicked.connect(self.update_sky)
    
    #region Signal Definitions
    def complete_random_sky(self):
        print("Complete Random Sky")
        CustomSkiesFunctions.execute_random_configurations()
        
    def moon_atmosphere_sky(self):
        print("Moon Atmosphere")
        sun_config = CustomSkiesFunctions.create_sun_config(
            sun_rotation=308.0,
            sun_intensity=1.0,
            sun_elevation=9.1,
            sun_size=5.3,
            altitude=0.9,
            air_density=0.0,
            dust_density=0.0,
            ozone_density=0.0
        )
        color_config = CustomSkiesFunctions.create_color_config(
            sky_color=[0.0, 0.0, 0.0],
            mix_factor=0.0
        )
        cloud_config = CustomSkiesFunctions.create_cloud_config(
            cloud_size=0.0,
            cloud_vector=[0.0, 0.0, 0.0],
            cloud_opacity=0.0,
            cloud_intensity=0.0,
            cloud_color=[0.0, 0.0, 0.0]
        )
        
        CustomSkiesFunctions.execute_config(
            sun_config, 
            color_config, 
            cloud_config
        )
        
    def dusty_atmosphere_sky(self):
        print("Dusty Atmosphere")
        sun_config = CustomSkiesFunctions.create_sun_config(
            sun_rotation=263.0,
            sun_intensity=2.8,
            sun_elevation=13.5,
            sun_size=10.6,
            altitude=0.5,
            air_density=10.0,
            dust_density=10.0,
            ozone_density=10.0
        )
        color_config = CustomSkiesFunctions.create_color_config(
            sky_color=[0.083, 0.041, 0.019],
            mix_factor=0.693
        )
        cloud_config = CustomSkiesFunctions.create_cloud_config(
            cloud_size=2.0,
            cloud_vector=[0.5, 0.5, 0.5],
            cloud_opacity=1.0,
            cloud_intensity=0.551,
            cloud_color=[1.0, 0.575, 0.239]
        )
        CustomSkiesFunctions.execute_config(
            sun_config, 
            color_config, 
            cloud_config
        )
    
    def soft_sunset_sky(self):
        print("Soft Sunset")
        sun_config = CustomSkiesFunctions.create_sun_config(
            sun_rotation=308.0,
            sun_intensity=2.8,
            sun_elevation=1.2,
            sun_size=19.5,
            altitude=0.9,
            air_density=1.154,
            dust_density=0.615,
            ozone_density=10.0
        )
        color_config = CustomSkiesFunctions.create_color_config(
            sky_color=[0.012, 0.006, 0.017],
            mix_factor=0.693
        )
        cloud_config = CustomSkiesFunctions.create_cloud_config(
            cloud_size=2.0,
            cloud_vector=[0.5, 0.5, 0.5],
            cloud_opacity=1.0,
            cloud_intensity=0.551,
            cloud_color=[1.0, 0.575, 0.239]
        )
        CustomSkiesFunctions.execute_config(
            sun_config,
            color_config,
            cloud_config
        )
    
    def harsh_sunset_sky(self):
        print("Harsh Sunset")
        sun_config = CustomSkiesFunctions.create_sun_config(
            sun_rotation=308.0,
            sun_intensity=2.8,
            sun_elevation=1.2,
            sun_size=5.5,
            altitude=0.9,
            air_density=1.154,
            dust_density=0.615,
            ozone_density=10.0
        )
        color_config = CustomSkiesFunctions.create_color_config(
            sky_color=[0.012, 0.006, 0.017],
            mix_factor=0.693
        )
        cloud_config = CustomSkiesFunctions.create_cloud_config(
            cloud_size=2.0,
            cloud_vector=[0.5, 0.5, 0.5],
            cloud_opacity=1.0,
            cloud_intensity=0.551,
            cloud_color=[1.0, 0.575, 0.239]
        )
        CustomSkiesFunctions.execute_config(
            sun_config,
            color_config,
            cloud_config
        )
        
    def cloudy_day_sky(self):
        print("Cloudy Day")
    
    def normal_day_sky(self):
        print("Normal Day")

    #region Update Sky With Custom Values
    def gather_values_from_ui(self):
        print("Gather Values")
        self.sun_rotation = self.sun_rotation_spin_box.value()
        self.sun_intensity = self.sun_intensity_spin_box.value()
        self.sun_elevation = self.sun_elevation_spin_box.value()
        self.sun_size = self.sun_size_spin_box.value()
        self.altitude = self.altitude_spin_box.value()
        self.air_density = self.air_density_spin_box.value()
        self.dust_density = self.dust_density_spin_box.value()
        self.ozone_density = self.ozone_density_spin_box.value()
        self.sky_color = (
            self.sky_color_x_spin_box.value(), 
            self.sky_color_y_spin_box.value(), 
            self.sky_color_z_spin_box.value(),
            1.0
        )
        self.mix_factor = self.mix_factor_spin_box.value()
        self.cloud_size = self.cloud_size_spin_box.value()
        self.cloud_vector = [
            self.cloud_vector_x_spin_box.value(), 
            self.cloud_vector_y_spin_box.value(), 
            self.cloud_vector_z_spin_box.value()]
        self.cloud_opacity = self.cloud_opacity_spin_box.value()
        self.cloud_intensity = self.cloud_intensity_spin_box.value()
        self.cloud_color = (
            self.cloud_color_x_spin_box.value(), 
            self.cloud_color_y_spin_box.value(), 
            self.cloud_color_z_spin_box.value(),
            1.0
        )
        
    def create_custom_configs(self):
        print("Create Configs")
        sun_config = CustomSkiesFunctions.create_sun_config(
            sun_rotation=self.sun_rotation,
            sun_intensity=self.sun_intensity,
            sun_elevation=self.sun_elevation,
            sun_size=self.sun_size,
            altitude=self.altitude,
            air_density=self.air_density,
            dust_density=self.dust_density,
            ozone_density=self.ozone_density
        )
        color_config = CustomSkiesFunctions.create_color_config(
            sky_color=self.sky_color,
            mix_factor=self.mix_factor
        )
        cloud_config = CustomSkiesFunctions.create_cloud_config(
            cloud_size=self.cloud_size,
            cloud_vector=self.cloud_vector,
            cloud_opacity=self.cloud_opacity,
            cloud_intensity=self.cloud_intensity,
            cloud_color=self.cloud_color
        )
        
        return sun_config, color_config, cloud_config
    
    def update_sky(self):
        print("Update Sky")
        self.gather_values_from_ui()
        sun_config, color_config, cloud_config = self.create_custom_configs()
        CustomSkiesFunctions.execute_config(
            sun_config, 
            color_config, 
            cloud_config
        )        
    #endregion
        
    #endregion
        
        
        

        
        
        
        
        