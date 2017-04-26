pyramid_oereb:

  language:
    - de
    - fr
    - it
    - rm

  flavour:
    - REDUCED
    - FULL
    - EMBEDDABLE

  app_schema:
    name: pyramid_oereb_main

  real_estate:
    source:
      class: pyramid_oereb.lib.sources.real_estate.RealEstateDatabaseSource
      params:
        db_connection: ${sqlalchemy_url}
        model: pyramid_oereb.models.PyramidOerebMainRealEstate

  address:
    source:
      class: pyramid_oereb.lib.sources.address.AddressDatabaseSource
      params:
        db_connection: ${sqlalchemy_url}
        model: pyramid_oereb.models.PyramidOerebMainAddress

  municipality:
    source:
      class: pyramid_oereb.lib.sources.municipality.MunicipalityDatabaseSource
      params:
        db_connection: ${sqlalchemy_url}
        model: pyramid_oereb.models.PyramidOerebMainMunicipality

  glossary:
    source:
      class: pyramid_oereb.lib.sources.glossary.GlossaryDatabaseSource
      params:
        db_connection: ${sqlalchemy_url}
        model: pyramid_oereb.models.PyramidOerebMainGlossary

  exclusion_of_liability:
    source:
      class: pyramid_oereb.lib.sources.exclusion_of_liability.ExclusionOfLiabilityDatabaseSource
      params:
        db_connection: ${sqlalchemy_url}
        model: pyramid_oereb.models.PyramidOerebMainExclusionOfLiability

  plrs:

    - name: plr73
      code: LandUsePlans
      geometry_type: LINESTRING
      label: Nutzungsplanung
      language: de

    - name: plr87
      code: MotorwaysProjectPlaningZones
      geometry_type: LINESTRING
      label: Projektierungszonen Nationalstrassen
      language: de

    - name: plr88
      code: MotorwaysBuildingLines
      geometry_type: LINESTRING
      label: Baulinien Nationalstrassen
      language: de

    - name: plr97
      code: RailwaysBuildingLines
      geometry_type: LINESTRING
      label: Baulinien Eisenbahnanlagen
      language: de

    - name: plr96
      code: RailwaysProjectPlanningZones
      geometry_type: POLYGON
      label: Projektierungszonen Eisenbahnanlagen
      language: de

    - name: plr103
      code: AirportsProjectPlanningZones
      geometry_type: POLYGON
      label: Projektierungszonen Flughafenanlagen
      language: de

    - name: plr104
      code: AirportsBuildingLines
      geometry_type: POLYGON
      label: Baulinien Flughafenanlagen
      language: de

    - name: plr108
      code: AirportsSecurityZonePlans
      geometry_type: POLYGON
      label: Sicherheitszonenplan Flughafen
      language: de

    - name: plr116
      code: ContaminatedSites
      geometry_type: POLYGON
      label: Belastete Standorte
      language: de

    - name: plr117
      code: ContaminatedMilitarySites
      geometry_type: POLYGON
      label: Belastete Standorte Militär
      language: de

    - name: plr118
      code: ContaminatedCivilAviationSites
      geometry_type: POLYGON
      label: Belastete Standorte Zivile Flugplätze
      language: de

    - name: plr119
      code: ContaminatedPublicTransportSites
      geometry_type: POLYGON
      label: Belastete Standorte Öeffentlicher Verkehr
      language: de

    - name: plr131
      code: GroundwaterProtectionZones
      geometry_type: POLYGON
      label: Grundwasserschutzzonen
      language: de

    - name: plr132
      code: GroundwaterProtectionSites
      geometry_type: POLYGON
      label: Grundwasserschutzareale
      language: de

    - name: plr145
      code: NoiseSensitivityLevels
      geometry_type: POLYGON
      label: Lärmemfindlichkeitsstufen
      language: de

    - name: plr157
      code: ForestPerimeters
      geometry_type: POLYGON
      label: Waldgrenzen
      language: de

    - name: plr159
      code: ForestDistanceLines
      geometry_type: POLYGON
      label: Waldabstandslinien
      language: de

  srid: 2056
  db_connection: ${sqlalchemy_url}