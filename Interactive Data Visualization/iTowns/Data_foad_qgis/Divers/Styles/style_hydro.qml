<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis labelsEnabled="0" maxScale="0" simplifyDrawingTol="1" readOnly="0" minScale="1e+8" simplifyDrawingHints="1" simplifyAlgorithm="0" hasScaleBasedVisibilityFlag="0" simplifyLocal="1" simplifyMaxScale="1" version="3.2.0-Bonn">
  <renderer-v2 forceraster="0" type="singleSymbol" symbollevels="0" enableorderby="0">
    <symbols>
      <symbol name="0" alpha="1" type="line" clip_to_extent="1">
        <layer pass="0" class="SimpleLine" locked="0" enabled="1">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="40,163,212,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="0.35" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <customproperties>
    <property value="0" key="embeddedWidgets/count"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer diagramType="Histogram" attributeLegend="1">
    <DiagramCategory backgroundColor="#ffffff" lineSizeType="MM" rotationOffset="270" barWidth="5" width="15" diagramOrientation="Up" height="15" labelPlacementMethod="XHeight" enabled="0" opacity="1" minScaleDenominator="0" backgroundAlpha="255" penColor="#000000" maxScaleDenominator="1e+8" scaleDependency="Area" penAlpha="255" sizeScale="3x:0,0,0,0,0,0" penWidth="0" scaleBasedVisibility="0" lineSizeScale="3x:0,0,0,0,0,0" minimumSize="0" sizeType="MM">
      <fontProperties style="" description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0"/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings placement="2" linePlacementFlags="18" obstacle="0" zIndex="0" dist="0" priority="0" showAll="1">
    <properties>
      <Option type="Map">
        <Option name="name" type="QString" value=""/>
        <Option name="properties"/>
        <Option name="type" type="QString" value="collection"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <fieldConfiguration>
    <field name="ID_BDCARTO">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="ETAT">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="LARGEUR">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="NATURE">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="NAVIGABLE">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="POS_SOL">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="TOPONYME">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="SENS">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="CLASSE">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias name="" field="ID_BDCARTO" index="0"/>
    <alias name="" field="ETAT" index="1"/>
    <alias name="" field="LARGEUR" index="2"/>
    <alias name="" field="NATURE" index="3"/>
    <alias name="" field="NAVIGABLE" index="4"/>
    <alias name="" field="POS_SOL" index="5"/>
    <alias name="" field="TOPONYME" index="6"/>
    <alias name="" field="SENS" index="7"/>
    <alias name="" field="CLASSE" index="8"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default field="ID_BDCARTO" applyOnUpdate="0" expression=""/>
    <default field="ETAT" applyOnUpdate="0" expression=""/>
    <default field="LARGEUR" applyOnUpdate="0" expression=""/>
    <default field="NATURE" applyOnUpdate="0" expression=""/>
    <default field="NAVIGABLE" applyOnUpdate="0" expression=""/>
    <default field="POS_SOL" applyOnUpdate="0" expression=""/>
    <default field="TOPONYME" applyOnUpdate="0" expression=""/>
    <default field="SENS" applyOnUpdate="0" expression=""/>
    <default field="CLASSE" applyOnUpdate="0" expression=""/>
  </defaults>
  <constraints>
    <constraint field="ID_BDCARTO" exp_strength="0" unique_strength="0" constraints="0" notnull_strength="0"/>
    <constraint field="ETAT" exp_strength="0" unique_strength="0" constraints="0" notnull_strength="0"/>
    <constraint field="LARGEUR" exp_strength="0" unique_strength="0" constraints="0" notnull_strength="0"/>
    <constraint field="NATURE" exp_strength="0" unique_strength="0" constraints="0" notnull_strength="0"/>
    <constraint field="NAVIGABLE" exp_strength="0" unique_strength="0" constraints="0" notnull_strength="0"/>
    <constraint field="POS_SOL" exp_strength="0" unique_strength="0" constraints="0" notnull_strength="0"/>
    <constraint field="TOPONYME" exp_strength="0" unique_strength="0" constraints="0" notnull_strength="0"/>
    <constraint field="SENS" exp_strength="0" unique_strength="0" constraints="0" notnull_strength="0"/>
    <constraint field="CLASSE" exp_strength="0" unique_strength="0" constraints="0" notnull_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint field="ID_BDCARTO" exp="" desc=""/>
    <constraint field="ETAT" exp="" desc=""/>
    <constraint field="LARGEUR" exp="" desc=""/>
    <constraint field="NATURE" exp="" desc=""/>
    <constraint field="NAVIGABLE" exp="" desc=""/>
    <constraint field="POS_SOL" exp="" desc=""/>
    <constraint field="TOPONYME" exp="" desc=""/>
    <constraint field="SENS" exp="" desc=""/>
    <constraint field="CLASSE" exp="" desc=""/>
  </constraintExpressions>
  <attributeactions>
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
  </attributeactions>
  <attributetableconfig sortExpression="" actionWidgetStyle="dropDown" sortOrder="0">
    <columns>
      <column name="ID_BDCARTO" hidden="0" width="-1" type="field"/>
      <column name="ETAT" hidden="0" width="-1" type="field"/>
      <column name="LARGEUR" hidden="0" width="-1" type="field"/>
      <column name="NATURE" hidden="0" width="-1" type="field"/>
      <column name="NAVIGABLE" hidden="0" width="-1" type="field"/>
      <column name="POS_SOL" hidden="0" width="-1" type="field"/>
      <column name="TOPONYME" hidden="0" width="-1" type="field"/>
      <column name="SENS" hidden="0" width="-1" type="field"/>
      <column name="CLASSE" hidden="0" width="-1" type="field"/>
      <column hidden="1" width="-1" type="actions"/>
    </columns>
  </attributetableconfig>
  <editform></editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath></editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
Les formulaires QGIS peuvent avoir une fonction Python qui sera appelée à l'ouverture du formulaire.

Utilisez cette fonction pour ajouter plus de fonctionnalités à vos formulaires.

Entrez le nom de la fonction dans le champ "Fonction d'initialisation Python".
Voici un exemple à suivre:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
    geom = feature.geometry()
    control = dialog.findChild(QWidget, "MyLineEdit")

]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field name="CLASSE" editable="1"/>
    <field name="ETAT" editable="1"/>
    <field name="ID_BDCARTO" editable="1"/>
    <field name="LARGEUR" editable="1"/>
    <field name="NATURE" editable="1"/>
    <field name="NAVIGABLE" editable="1"/>
    <field name="POS_SOL" editable="1"/>
    <field name="SENS" editable="1"/>
    <field name="TOPONYME" editable="1"/>
  </editable>
  <labelOnTop>
    <field name="CLASSE" labelOnTop="0"/>
    <field name="ETAT" labelOnTop="0"/>
    <field name="ID_BDCARTO" labelOnTop="0"/>
    <field name="LARGEUR" labelOnTop="0"/>
    <field name="NATURE" labelOnTop="0"/>
    <field name="NAVIGABLE" labelOnTop="0"/>
    <field name="POS_SOL" labelOnTop="0"/>
    <field name="SENS" labelOnTop="0"/>
    <field name="TOPONYME" labelOnTop="0"/>
  </labelOnTop>
  <widgets/>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <expressionfields/>
  <previewExpression>ID_BDCARTO</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>1</layerGeometryType>
</qgis>
