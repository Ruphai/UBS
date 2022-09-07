<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis version="1.8.0-Lisboa" minimumScale="0" maximumScale="1e+08" hasScaleBasedVisibilityFlag="0">
  <transparencyLevelInt>255</transparencyLevelInt>
  <renderer-v2 attr="DEGRE" symbollevels="0" type="categorizedSymbol">
    <categories>
      <category symbol="0" value="ZI faible naturelle" label="ZI faible naturelle"/>
      <category symbol="1" value="ZI faible urbaine" label="ZI faible urbaine"/>
      <category symbol="2" value="ZI forte naturelle" label="ZI forte naturelle"/>
      <category symbol="3" value="ZI forte urbaine" label="ZI forte urbaine"/>
      <category symbol="4" value="ZI moyenne naturelle" label="ZI moyenne naturelle"/>
      <category symbol="5" value="ZI moyenne urbaine" label="ZI moyenne urbaine"/>
      <category symbol="6" value="" label=""/>
    </categories>
    <symbols>
      <symbol outputUnit="MM" alpha="1" type="fill" name="0">
        <layer pass="0" class="SimpleFill" locked="0">
          <prop k="color" v="85,170,0,255"/>
          <prop k="color_border" v="85,170,0,255"/>
          <prop k="offset" v="0,0"/>
          <prop k="style" v="dense6"/>
          <prop k="style_border" v="solid"/>
          <prop k="width_border" v="0.26"/>
        </layer>
      </symbol>
      <symbol outputUnit="MM" alpha="1" type="fill" name="1">
        <layer pass="0" class="SimpleFill" locked="0">
          <prop k="color" v="255,0,0,255"/>
          <prop k="color_border" v="255,0,0,255"/>
          <prop k="offset" v="0,0"/>
          <prop k="style" v="dense6"/>
          <prop k="style_border" v="solid"/>
          <prop k="width_border" v="0.26"/>
        </layer>
      </symbol>
      <symbol outputUnit="MM" alpha="1" type="fill" name="2">
        <layer pass="0" class="SimpleFill" locked="0">
          <prop k="color" v="85,170,0,255"/>
          <prop k="color_border" v="85,170,0,255"/>
          <prop k="offset" v="0,0"/>
          <prop k="style" v="solid"/>
          <prop k="style_border" v="solid"/>
          <prop k="width_border" v="0.26"/>
        </layer>
      </symbol>
      <symbol outputUnit="MM" alpha="1" type="fill" name="3">
        <layer pass="0" class="SimpleFill" locked="0">
          <prop k="color" v="255,0,0,255"/>
          <prop k="color_border" v="255,0,0,255"/>
          <prop k="offset" v="0,0"/>
          <prop k="style" v="solid"/>
          <prop k="style_border" v="solid"/>
          <prop k="width_border" v="0.26"/>
        </layer>
      </symbol>
      <symbol outputUnit="MM" alpha="1" type="fill" name="4">
        <layer pass="0" class="SimpleFill" locked="0">
          <prop k="color" v="85,170,0,255"/>
          <prop k="color_border" v="85,170,0,255"/>
          <prop k="offset" v="0,0"/>
          <prop k="style" v="dense3"/>
          <prop k="style_border" v="solid"/>
          <prop k="width_border" v="0.26"/>
        </layer>
      </symbol>
      <symbol outputUnit="MM" alpha="1" type="fill" name="5">
        <layer pass="0" class="SimpleFill" locked="0">
          <prop k="color" v="255,0,0,255"/>
          <prop k="color_border" v="255,0,0,255"/>
          <prop k="offset" v="0,0"/>
          <prop k="style" v="dense3"/>
          <prop k="style_border" v="solid"/>
          <prop k="width_border" v="0.26"/>
        </layer>
      </symbol>
      <symbol outputUnit="MM" alpha="1" type="fill" name="6">
        <layer pass="0" class="SimpleFill" locked="0">
          <prop k="color" v="0,0,255,255"/>
          <prop k="color_border" v="0,0,0,255"/>
          <prop k="offset" v="0,0"/>
          <prop k="style" v="solid"/>
          <prop k="style_border" v="solid"/>
          <prop k="width_border" v="0.26"/>
        </layer>
      </symbol>
    </symbols>
    <source-symbol>
      <symbol outputUnit="MM" alpha="1" type="fill" name="0">
        <layer pass="0" class="SimpleFill" locked="0">
          <prop k="color" v="11,198,8,255"/>
          <prop k="color_border" v="0,0,0,255"/>
          <prop k="offset" v="0,0"/>
          <prop k="style" v="solid"/>
          <prop k="style_border" v="solid"/>
          <prop k="width_border" v="0.26"/>
        </layer>
      </symbol>
    </source-symbol>
    <colorramp type="gradient" name="[source]">
      <prop k="color1" v="255,0,0,255"/>
      <prop k="color2" v="0,0,255,255"/>
      <prop k="stops" v="0.5;255,255,0,255"/>
    </colorramp>
    <rotation field=""/>
    <sizescale field=""/>
  </renderer-v2>
  <customproperties/>
  <displayfield>COMMUNE</displayfield>
  <label>0</label>
  <labelattributes>
    <label fieldname="" text="Étiquette"/>
    <family fieldname="" name="MS Shell Dlg 2"/>
    <size fieldname="" units="pt" value="12"/>
    <bold fieldname="" on="0"/>
    <italic fieldname="" on="0"/>
    <underline fieldname="" on="0"/>
    <strikeout fieldname="" on="0"/>
    <color fieldname="" red="0" blue="0" green="0"/>
    <x fieldname=""/>
    <y fieldname=""/>
    <offset x="0" y="0" units="pt" yfieldname="" xfieldname=""/>
    <angle fieldname="" value="0" auto="0"/>
    <alignment fieldname="" value="center"/>
    <buffercolor fieldname="" red="255" blue="255" green="255"/>
    <buffersize fieldname="" units="pt" value="1"/>
    <bufferenabled fieldname="" on=""/>
    <multilineenabled fieldname="" on=""/>
    <selectedonly on=""/>
  </labelattributes>
  <edittypes>
    <edittype type="0" name="COMMUNE"/>
    <edittype type="0" name="DEGRE"/>
    <edittype type="0" name="TYPE"/>
  </edittypes>
  <editform>.</editform>
  <editforminit></editforminit>
  <annotationform>.</annotationform>
  <attributeactions/>
</qgis>
