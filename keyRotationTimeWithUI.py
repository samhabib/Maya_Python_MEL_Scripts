// Warning: file: C:/Program Files/Autodesk/Maya2017/scripts/startup/shelf.mel line 205: The shelf "RenderMan" already exists.
 // 
onSetCurrentLayout "Animation";
file -f -new;
preferredRenderer -makeCurrent;
// Warning: file: C:/Program Files/Autodesk/Maya2017/scripts/startup/rememberViewportSettings.mel line 29: Active stereo does not work with Aero enabled. Active stereo has been disabled. // 
// untitled // 
commandPort -securityWarning -name commandportDefault;
// AbcExport v1.0 using Alembic 1.5.8 (built Dec 24 2015 17:28:19)
updateRendererUI;
evalDeferred "shaderBallRendererMenuUpdate";
// Pixar's RfM 21.4 (@1747743 May 17 2017), RMS 21.4, RenderMan 21.4 @1747743
// Warning: file: C:/Program Files/Autodesk/Maya2017/scripts/startup/autoLoadPlugin.mel line 32: Loading plug-in "RenderMan_for_Maya" has resulted in changes to the scene that may need to be saved. // 
# pymel.core : Updating pymel with pre-loaded plugins: mayaHIK, invertShape, GamePipeline, CloudImportExport, curveWarp, tiffFloatReader, MASH, poseInterpolator, bifrostvisplugin, ATFPlugin, hairPhysicalShader, ikSpringSolver, ik2Bsolver, xgenToolkit, AbcExport, retargeterNodes, gameFbxExporter, VectorRender, OpenEXRLoader, lookdevKit, Unfold3D, Type, mayaCharacterization, RenderMan_for_Maya, modelingToolkit, deformerEvaluator, renderSetup, GPUBuiltInDeformer, fbxmaya
evalDeferred "shaderBallRendererMenuUpdate";
import arnold
// Successfully imported python module 'arnold'
import mtoa
// Successfully imported python module 'mtoa'
import mtoa.cmds.registerArnoldRenderer;mtoa.cmds.registerArnoldRenderer.registerArnoldRenderer()
Maya 2017 importing module pymel 1.0.9 (C:\Program Files\Autodesk\Maya2017\Python\lib\site-packages\pymel\__init__.py)
// Successfully registered renderer 'arnold'
// AbcImport v1.0 using Alembic 1.5.8 (built Dec 24 2015 17:28:19)
updateRendererUI;
updateRendererUI;
// Warning: };
 // 
// Warning: "C:/Program Files/Autodesk/Maya2017/scripts/others/imageFormats.mel" line 65.2 : Global variable is already initialized; this occurrence is ignored. // 
file -f -options "v=0;"  -ignoreVersion  -typ "mayaAscii" -o "C:/Users/samha_000/Documents/Sam_Habib_B23/assets/Sams_r1_geo.ma";addRecentFile("C:/Users/samha_000/Documents/Sam_Habib_B23/assets/Sams_r1_geo.ma", "mayaAscii");
closeAllNodeEditors;
closeHypershade;
updateRenderOverride;
// Warning: line 2367: The default image may not be modified. Use the -i/image flag instead. // 
// File read in  2.2 seconds.
select -r root_geo ;
selectKey -clear ;
// 0 // 
toggleVisibilityAndKeepSelection `optionVar -query toggleVisibilityAndKeepSelectionBehaviour`;
select -r root_geo ;
selectKey -clear ;
// 0 // 
toggleVisibilityAndKeepSelection `optionVar -query toggleVisibilityAndKeepSelectionBehaviour`;
select -cl  ;
select -r root_jnt ;
selectKey -clear ;
// 0 // 
select -r chest_jnt ;
select -cl  ;
select -r l_hand_geo ;
displaySmoothness -divisionsU 0 -divisionsV 0 -pointsWire 4 -pointsShaded 1 -polygonObject 1;
displaySmoothness -divisionsU 3 -divisionsV 3 -pointsWire 16 -pointsShaded 4 -polygonObject 3;
displaySmoothness -divisionsU 0 -divisionsV 0 -pointsWire 4 -pointsShaded 1 -polygonObject 1;
displaySmoothness -divisionsU 3 -divisionsV 3 -pointsWire 16 -pointsShaded 4 -polygonObject 3;
select -cl  ;
select -r l_hand_geo ;
displaySmoothness -divisionsU 0 -divisionsV 0 -pointsWire 4 -pointsShaded 1 -polygonObject 1;
select -cl  ;
SnapToPoint; dR_enterForSnap;
select -r l_hand_geo ;
isolateSelect -state 1 modelPanel4;
select -r l_hand_geo ;
isolateSelect -state 0 modelPanel4;
isolateSelect -state 1 modelPanel4;
select -r l_hand_geo.vtx[0:766] ;
move -r -os -wd 3.831675 0 0 ;
move -r -os -wd -2.479265 0 0 ;
// Undo: move -r -os -wd -2.479265 0 0 
// Undo: move -r -os -wd 3.831675 0 0 
isolateSelect -state 0 modelPanel4;
select -cl  ;
displaySmoothness -divisionsU 0 -divisionsV 0 -pointsWire 4 -pointsShaded 1 -polygonObject 1;
displaySmoothness -divisionsU 3 -divisionsV 3 -pointsWire 16 -pointsShaded 4 -polygonObject 3;
displaySmoothness -divisionsU 0 -divisionsV 0 -pointsWire 4 -pointsShaded 1 -polygonObject 1;
displaySmoothness -divisionsU 3 -divisionsV 3 -pointsWire 16 -pointsShaded 4 -polygonObject 3;
displaySmoothness -divisionsU 3 -divisionsV 3 -pointsWire 16 -pointsShaded 4 -polygonObject 3;
displaySmoothness -divisionsU 0 -divisionsV 0 -pointsWire 4 -pointsShaded 1 -polygonObject 1;
isolateSelect -state 1 modelPanel4;
isolateSelect -state 0 modelPanel4;
select -r l_hand_geo.vtx[503] ;
select -d l_hand_geo.vtx[503] ;
select -r l_hand_geo ;
isolateSelect -state 1 modelPanel4;
select -add l_hand_geo.vtx[503] ;
select -r l_hand_geo.vtx[0:766] ;
setAttr "l_hand_geoShape.pnts[0].pntx" 0;
setAttr "l_hand_geoShape.pnts[1].pntx" 0;
setAttr "l_hand_geoShape.pnts[2].pntx" 0;
setAttr "l_hand_geoShape.pnts[3].pntx" 0;
setAttr "l_hand_geoShape.pnts[4].pntx" 0;
setAttr "l_hand_geoShape.pnts[5].pntx" 0;
setAttr "l_hand_geoShape.pnts[6].pntx" 0;
setAttr "l_hand_geoShape.pnts[7].pntx" 0;
setAttr "l_hand_geoShape.pnts[8].pntx" 0;
setAttr "l_hand_geoShape.pnts[9].pntx" 0;
setAttr "l_hand_geoShape.pnts[10].pntx" 0;
setAttr "l_hand_geoShape.pnts[11].pntx" 0;
setAttr "l_hand_geoShape.pnts[12].pntx" 0;
setAttr "l_hand_geoShape.pnts[13].pntx" 0;
setAttr "l_hand_geoShape.pnts[14].pntx" 0;
setAttr "l_hand_geoShape.pnts[15].pntx" 0;
setAttr "l_hand_geoShape.pnts[16].pntx" 0;
setAttr "l_hand_geoShape.pnts[17].pntx" 0;
setAttr "l_hand_geoShape.pnts[18].pntx" 0;
setAttr "l_hand_geoShape.pnts[19].pntx" 0;
setAttr "l_hand_geoShape.pnts[20].pntx" 0;
setAttr "l_hand_geoShape.pnts[21].pntx" 0;
setAttr "l_hand_geoShape.pnts[22].pntx" 0;
setAttr "l_hand_geoShape.pnts[23].pntx" 0;
setAttr "l_hand_geoShape.pnts[24].pntx" 0;
setAttr "l_hand_geoShape.pnts[25].pntx" 0;
setAttr "l_hand_geoShape.pnts[26].pntx" 0;
setAttr "l_hand_geoShape.pnts[27].pntx" 0;
setAttr "l_hand_geoShape.pnts[28].pntx" 0;
setAttr "l_hand_geoShape.pnts[29].pntx" 0;
setAttr "l_hand_geoShape.pnts[30].pntx" 0;
setAttr "l_hand_geoShape.pnts[31].pntx" 0;
setAttr "l_hand_geoShape.pnts[32].pntx" 0;
setAttr "l_hand_geoShape.pnts[33].pntx" 0;
setAttr "l_hand_geoShape.pnts[34].pntx" 0;
setAttr "l_hand_geoShape.pnts[35].pntx" 0;
setAttr "l_hand_geoShape.pnts[36].pntx" 0;
setAttr "l_hand_geoShape.pnts[37].pntx" 0;
setAttr "l_hand_geoShape.pnts[38].pntx" 0;
setAttr "l_hand_geoShape.pnts[39].pntx" 0;
setAttr "l_hand_geoShape.pnts[40].pntx" 0;
setAttr "l_hand_geoShape.pnts[41].pntx" 0;
setAttr "l_hand_geoShape.pnts[42].pntx" 0;
setAttr "l_hand_geoShape.pnts[43].pntx" 0;
setAttr "l_hand_geoShape.pnts[44].pntx" 0;
setAttr "l_hand_geoShape.pnts[45].pntx" 0;
setAttr "l_hand_geoShape.pnts[46].pntx" 0;
setAttr "l_hand_geoShape.pnts[47].pntx" 0;
setAttr "l_hand_geoShape.pnts[48].pntx" 0;
setAttr "l_hand_geoShape.pnts[49].pntx" 0;
setAttr "l_hand_geoShape.pnts[50].pntx" 0;
setAttr "l_hand_geoShape.pnts[51].pntx" 0;
setAttr "l_hand_geoShape.pnts[52].pntx" 0;
setAttr "l_hand_geoShape.pnts[53].pntx" 0;
setAttr "l_hand_geoShape.pnts[54].pntx" 0;
setAttr "l_hand_geoShape.pnts[55].pntx" 0;
setAttr "l_hand_geoShape.pnts[56].pntx" 0;
setAttr "l_hand_geoShape.pnts[57].pntx" 0;
setAttr "l_hand_geoShape.pnts[58].pntx" 0;
setAttr "l_hand_geoShape.pnts[59].pntx" 0;
setAttr "l_hand_geoShape.pnts[60].pntx" 0;
setAttr "l_hand_geoShape.pnts[61].pntx" 0;
setAttr "l_hand_geoShape.pnts[62].pntx" 0;
setAttr "l_hand_geoShape.pnts[63].pntx" 0;
setAttr "l_hand_geoShape.pnts[64].pntx" 0;
setAttr "l_hand_geoShape.pnts[65].pntx" 0;
setAttr "l_hand_geoShape.pnts[66].pntx" 0;
setAttr "l_hand_geoShape.pnts[67].pntx" 0;
setAttr "l_hand_geoShape.pnts[68].pntx" 0;
setAttr "l_hand_geoShape.pnts[69].pntx" 0;
setAttr "l_hand_geoShape.pnts[70].pntx" 0;
setAttr "l_hand_geoShape.pnts[71].pntx" 0;
setAttr "l_hand_geoShape.pnts[72].pntx" 0;
setAttr "l_hand_geoShape.pnts[73].pntx" 0;
setAttr "l_hand_geoShape.pnts[74].pntx" 0;
setAttr "l_hand_geoShape.pnts[75].pntx" 0;
setAttr "l_hand_geoShape.pnts[76].pntx" 0;
setAttr "l_hand_geoShape.pnts[77].pntx" 0;
setAttr "l_hand_geoShape.pnts[78].pntx" 0;
setAttr "l_hand_geoShape.pnts[79].pntx" 0;
setAttr "l_hand_geoShape.pnts[80].pntx" 0;
setAttr "l_hand_geoShape.pnts[81].pntx" 0;
setAttr "l_hand_geoShape.pnts[82].pntx" 0;
setAttr "l_hand_geoShape.pnts[83].pntx" 0;
setAttr "l_hand_geoShape.pnts[84].pntx" 0;
setAttr "l_hand_geoShape.pnts[85].pntx" 0;
setAttr "l_hand_geoShape.pnts[86].pntx" 0;
setAttr "l_hand_geoShape.pnts[87].pntx" 0;
setAttr "l_hand_geoShape.pnts[88].pntx" 0;
setAttr "l_hand_geoShape.pnts[89].pntx" 0;
setAttr "l_hand_geoShape.pnts[90].pntx" 0;
setAttr "l_hand_geoShape.pnts[91].pntx" 0;
setAttr "l_hand_geoShape.pnts[92].pntx" 0;
setAttr "l_hand_geoShape.pnts[93].pntx" 0;
setAttr "l_hand_geoShape.pnts[94].pntx" 0;
setAttr "l_hand_geoShape.pnts[95].pntx" 0;
setAttr "l_hand_geoShape.pnts[96].pntx" 0;
setAttr "l_hand_geoShape.pnts[97].pntx" 0;
setAttr "l_hand_geoShape.pnts[98].pntx" 0;
setAttr "l_hand_geoShape.pnts[99].pntx" 0;
setAttr "l_hand_geoShape.pnts[100].pntx" 0;
setAttr "l_hand_geoShape.pnts[101].pntx" 0;
setAttr "l_hand_geoShape.pnts[102].pntx" 0;
setAttr "l_hand_geoShape.pnts[103].pntx" 0;
setAttr "l_hand_geoShape.pnts[104].pntx" 0;
setAttr "l_hand_geoShape.pnts[105].pntx" 0;
setAttr "l_hand_geoShape.pnts[106].pntx" 0;
setAttr "l_hand_geoShape.pnts[107].pntx" 0;
setAttr "l_hand_geoShape.pnts[108].pntx" 0;
setAttr "l_hand_geoShape.pnts[109].pntx" 0;
setAttr "l_hand_geoShape.pnts[110].pntx" 0;
setAttr "l_hand_geoShape.pnts[111].pntx" 0;
setAttr "l_hand_geoShape.pnts[112].pntx" 0;
setAttr "l_hand_geoShape.pnts[113].pntx" 0;
setAttr "l_hand_geoShape.pnts[114].pntx" 0;
setAttr "l_hand_geoShape.pnts[115].pntx" 0;
setAttr "l_hand_geoShape.pnts[116].pntx" 0;
setAttr "l_hand_geoShape.pnts[117].pntx" 0;
setAttr "l_hand_geoShape.pnts[118].pntx" 0;
setAttr "l_hand_geoShape.pnts[119].pntx" 0;
setAttr "l_hand_geoShape.pnts[120].pntx" 0;
setAttr "l_hand_geoShape.pnts[121].pntx" 0;
setAttr "l_hand_geoShape.pnts[122].pntx" 0;
setAttr "l_hand_geoShape.pnts[123].pntx" 0;
setAttr "l_hand_geoShape.pnts[124].pntx" 0;
setAttr "l_hand_geoShape.pnts[125].pntx" 0;
setAttr "l_hand_geoShape.pnts[126].pntx" 0;
setAttr "l_hand_geoShape.pnts[127].pntx" 0;
setAttr "l_hand_geoShape.pnts[128].pntx" 0;
setAttr "l_hand_geoShape.pnts[129].pntx" 0;
setAttr "l_hand_geoShape.pnts[130].pntx" 0;
setAttr "l_hand_geoShape.pnts[131].pntx" 0;
setAttr "l_hand_geoShape.pnts[132].pntx" 0;
setAttr "l_hand_geoShape.pnts[133].pntx" 0;
setAttr "l_hand_geoShape.pnts[134].pntx" 0;
setAttr "l_hand_geoShape.pnts[135].pntx" 0;
setAttr "l_hand_geoShape.pnts[136].pntx" 0;
setAttr "l_hand_geoShape.pnts[137].pntx" 0;
setAttr "l_hand_geoShape.pnts[138].pntx" 0;
setAttr "l_hand_geoShape.pnts[139].pntx" 0;
setAttr "l_hand_geoShape.pnts[140].pntx" 0;
setAttr "l_hand_geoShape.pnts[141].pntx" 0;
setAttr "l_hand_geoShape.pnts[142].pntx" 0;
setAttr "l_hand_geoShape.pnts[143].pntx" 0;
setAttr "l_hand_geoShape.pnts[144].pntx" 0;
setAttr "l_hand_geoShape.pnts[145].pntx" 0;
setAttr "l_hand_geoShape.pnts[146].pntx" 0;
setAttr "l_hand_geoShape.pnts[147].pntx" 0;
setAttr "l_hand_geoShape.pnts[148].pntx" 0;
setAttr "l_hand_geoShape.pnts[149].pntx" 0;
setAttr "l_hand_geoShape.pnts[150].pntx" 0;
setAttr "l_hand_geoShape.pnts[151].pntx" 0;
setAttr "l_hand_geoShape.pnts[152].pntx" 0;
setAttr "l_hand_geoShape.pnts[153].pntx" 0;
setAttr "l_hand_geoShape.pnts[154].pntx" 0;
setAttr "l_hand_geoShape.pnts[155].pntx" 0;
setAttr "l_hand_geoShape.pnts[156].pntx" 0;
setAttr "l_hand_geoShape.pnts[157].pntx" 0;
setAttr "l_hand_geoShape.pnts[158].pntx" 0;
setAttr "l_hand_geoShape.pnts[159].pntx" 0;
setAttr "l_hand_geoShape.pnts[160].pntx" 0;
setAttr "l_hand_geoShape.pnts[161].pntx" 0;
setAttr "l_hand_geoShape.pnts[162].pntx" 0;
setAttr "l_hand_geoShape.pnts[163].pntx" 0;
setAttr "l_hand_geoShape.pnts[164].pntx" 0;
setAttr "l_hand_geoShape.pnts[165].pntx" 0;
setAttr "l_hand_geoShape.pnts[166].pntx" 0;
setAttr "l_hand_geoShape.pnts[167].pntx" 0;
setAttr "l_hand_geoShape.pnts[168].pntx" 0;
setAttr "l_hand_geoShape.pnts[169].pntx" 0;
setAttr "l_hand_geoShape.pnts[170].pntx" 0;
setAttr "l_hand_geoShape.pnts[171].pntx" 0;
setAttr "l_hand_geoShape.pnts[172].pntx" 0;
setAttr "l_hand_geoShape.pnts[173].pntx" 0;
setAttr "l_hand_geoShape.pnts[174].pntx" 0;
setAttr "l_hand_geoShape.pnts[175].pntx" 0;
setAttr "l_hand_geoShape.pnts[176].pntx" 0;
setAttr "l_hand_geoShape.pnts[177].pntx" 0;
setAttr "l_hand_geoShape.pnts[178].pntx" 0;
setAttr "l_hand_geoShape.pnts[179].pntx" 0;
setAttr "l_hand_geoShape.pnts[180].pntx" 0;
setAttr "l_hand_geoShape.pnts[181].pntx" 0;
setAttr "l_hand_geoShape.pnts[182].pntx" 0;
setAttr "l_hand_geoShape.pnts[183].pntx" 0;
setAttr "l_hand_geoShape.pnts[184].pntx" 0;
setAttr "l_hand_geoShape.pnts[185].pntx" 0;
setAttr "l_hand_geoShape.pnts[186].pntx" 0;
setAttr "l_hand_geoShape.pnts[187].pntx" 0;
setAttr "l_hand_geoShape.pnts[188].pntx" 0;
setAttr "l_hand_geoShape.pnts[189].pntx" 0;
setAttr "l_hand_geoShape.pnts[190].pntx" 0;
setAttr "l_hand_geoShape.pnts[191].pntx" 0;
setAttr "l_hand_geoShape.pnts[192].pntx" 0;
setAttr "l_hand_geoShape.pnts[193].pntx" 0;
setAttr "l_hand_geoShape.pnts[194].pntx" 0;
setAttr "l_hand_geoShape.pnts[195].pntx" 0;
setAttr "l_hand_geoShape.pnts[196].pntx" 0;
setAttr "l_hand_geoShape.pnts[197].pntx" 0;
setAttr "l_hand_geoShape.pnts[198].pntx" 0;
setAttr "l_hand_geoShape.pnts[199].pntx" 0;
setAttr "l_hand_geoShape.pnts[200].pntx" 0;
setAttr "l_hand_geoShape.pnts[201].pntx" 0;
setAttr "l_hand_geoShape.pnts[202].pntx" 0;
setAttr "l_hand_geoShape.pnts[203].pntx" 0;
setAttr "l_hand_geoShape.pnts[204].pntx" 0;
setAttr "l_hand_geoShape.pnts[205].pntx" 0;
setAttr "l_hand_geoShape.pnts[206].pntx" 0;
setAttr "l_hand_geoShape.pnts[207].pntx" 0;
setAttr "l_hand_geoShape.pnts[208].pntx" 0;
setAttr "l_hand_geoShape.pnts[209].pntx" 0;
setAttr "l_hand_geoShape.pnts[210].pntx" 0;
setAttr "l_hand_geoShape.pnts[211].pntx" 0;
setAttr "l_hand_geoShape.pnts[212].pntx" 0;
setAttr "l_hand_geoShape.pnts[213].pntx" 0;
setAttr "l_hand_geoShape.pnts[214].pntx" 0;
setAttr "l_hand_geoShape.pnts[215].pntx" 0;
setAttr "l_hand_geoShape.pnts[216].pntx" 0;
setAttr "l_hand_geoShape.pnts[217].pntx" 0;
setAttr "l_hand_geoShape.pnts[218].pntx" 0;
setAttr "l_hand_geoShape.pnts[219].pntx" 0;
setAttr "l_hand_geoShape.pnts[220].pntx" 0;
setAttr "l_hand_geoShape.pnts[221].pntx" 0;
setAttr "l_hand_geoShape.pnts[222].pntx" 0;
setAttr "l_hand_geoShape.pnts[223].pntx" 0;
setAttr "l_hand_geoShape.pnts[224].pntx" 0;
setAttr "l_hand_geoShape.pnts[225].pntx" 0;
setAttr "l_hand_geoShape.pnts[226].pntx" 0;
setAttr "l_hand_geoShape.pnts[227].pntx" 0;
setAttr "l_hand_geoShape.pnts[228].pntx" 0;
setAttr "l_hand_geoShape.pnts[229].pntx" 0;
setAttr "l_hand_geoShape.pnts[230].pntx" 0;
setAttr "l_hand_geoShape.pnts[231].pntx" 0;
setAttr "l_hand_geoShape.pnts[232].pntx" 0;
setAttr "l_hand_geoShape.pnts[233].pntx" 0;
setAttr "l_hand_geoShape.pnts[234].pntx" 0;
setAttr "l_hand_geoShape.pnts[235].pntx" 0;
setAttr "l_hand_geoShape.pnts[236].pntx" 0;
setAttr "l_hand_geoShape.pnts[237].pntx" 0;
setAttr "l_hand_geoShape.pnts[238].pntx" 0;
setAttr "l_hand_geoShape.pnts[239].pntx" 0;
setAttr "l_hand_geoShape.pnts[240].pntx" 0;
setAttr "l_hand_geoShape.pnts[241].pntx" 0;
setAttr "l_hand_geoShape.pnts[242].pntx" 0;
setAttr "l_hand_geoShape.pnts[243].pntx" 0;
setAttr "l_hand_geoShape.pnts[244].pntx" 0;
setAttr "l_hand_geoShape.pnts[245].pntx" 0;
setAttr "l_hand_geoShape.pnts[246].pntx" 0;
setAttr "l_hand_geoShape.pnts[247].pntx" 0;
setAttr "l_hand_geoShape.pnts[248].pntx" 0;
setAttr "l_hand_geoShape.pnts[249].pntx" 0;
setAttr "l_hand_geoShape.pnts[250].pntx" 0;
setAttr "l_hand_geoShape.pnts[251].pntx" 0;
setAttr "l_hand_geoShape.pnts[252].pntx" 0;
setAttr "l_hand_geoShape.pnts[253].pntx" 0;
setAttr "l_hand_geoShape.pnts[254].pntx" 0;
setAttr "l_hand_geoShape.pnts[255].pntx" 0;
setAttr "l_hand_geoShape.pnts[256].pntx" 0;
setAttr "l_hand_geoShape.pnts[257].pntx" 0;
setAttr "l_hand_geoShape.pnts[258].pntx" 0;
setAttr "l_hand_geoShape.pnts[259].pntx" 0;
setAttr "l_hand_geoShape.pnts[260].pntx" 0;
setAttr "l_hand_geoShape.pnts[261].pntx" 0;
setAttr "l_hand_geoShape.pnts[262].pntx" 0;
setAttr "l_hand_geoShape.pnts[263].pntx" 0;
setAttr "l_hand_geoShape.pnts[264].pntx" 0;
setAttr "l_hand_geoShape.pnts[265].pntx" 0;
setAttr "l_hand_geoShape.pnts[266].pntx" 0;
setAttr "l_hand_geoShape.pnts[267].pntx" 0;
setAttr "l_hand_geoShape.pnts[268].pntx" 0;
setAttr "l_hand_geoShape.pnts[269].pntx" 0;
setAttr "l_hand_geoShape.pnts[270].pntx" 0;
setAttr "l_hand_geoShape.pnts[271].pntx" 0;
setAttr "l_hand_geoShape.pnts[272].pntx" 0;
setAttr "l_hand_geoShape.pnts[273].pntx" 0;
setAttr "l_hand_geoShape.pnts[274].pntx" 0;
setAttr "l_hand_geoShape.pnts[275].pntx" 0;
setAttr "l_hand_geoShape.pnts[276].pntx" 0;
setAttr "l_hand_geoShape.pnts[277].pntx" 0;
setAttr "l_hand_geoShape.pnts[278].pntx" 0;
setAttr "l_hand_geoShape.pnts[279].pntx" 0;
setAttr "l_hand_geoShape.pnts[280].pntx" 0;
setAttr "l_hand_geoShape.pnts[281].pntx" 0;
setAttr "l_hand_geoShape.pnts[282].pntx" 0;
setAttr "l_hand_geoShape.pnts[283].pntx" 0;
setAttr "l_hand_geoShape.pnts[284].pntx" 0;
setAttr "l_hand_geoShape.pnts[285].pntx" 0;
setAttr "l_hand_geoShape.pnts[286].pntx" 0;
setAttr "l_hand_geoShape.pnts[287].pntx" 0;
setAttr "l_hand_geoShape.pnts[288].pntx" 0;
setAttr "l_hand_geoShape.pnts[289].pntx" 0;
setAttr "l_hand_geoShape.pnts[290].pntx" 0;
setAttr "l_hand_geoShape.pnts[291].pntx" 0;
setAttr "l_hand_geoShape.pnts[292].pntx" 0;
setAttr "l_hand_geoShape.pnts[293].pntx" 0;
setAttr "l_hand_geoShape.pnts[294].pntx" 0;
setAttr "l_hand_geoShape.pnts[295].pntx" 0;
setAttr "l_hand_geoShape.pnts[296].pntx" 0;
setAttr "l_hand_geoShape.pnts[297].pntx" 0;
setAttr "l_hand_geoShape.pnts[298].pntx" 0;
setAttr "l_hand_geoShape.pnts[299].pntx" 0;
setAttr "l_hand_geoShape.pnts[300].pntx" 0;
setAttr "l_hand_geoShape.pnts[301].pntx" 0;
setAttr "l_hand_geoShape.pnts[302].pntx" 0;
setAttr "l_hand_geoShape.pnts[303].pntx" 0;
setAttr "l_hand_geoShape.pnts[304].pntx" 0;
setAttr "l_hand_geoShape.pnts[305].pntx" 0;
setAttr "l_hand_geoShape.pnts[306].pntx" 0;
setAttr "l_hand_geoShape.pnts[307].pntx" 0;
setAttr "l_hand_geoShape.pnts[308].pntx" 0;
setAttr "l_hand_geoShape.pnts[309].pntx" 0;
setAttr "l_hand_geoShape.pnts[310].pntx" 0;
setAttr "l_hand_geoShape.pnts[311].pntx" 0;
setAttr "l_hand_geoShape.pnts[312].pntx" 0;
setAttr "l_hand_geoShape.pnts[313].pntx" 0;
setAttr "l_hand_geoShape.pnts[314].pntx" 0;
setAttr "l_hand_geoShape.pnts[315].pntx" 0;
setAttr "l_hand_geoShape.pnts[316].pntx" 0;
setAttr "l_hand_geoShape.pnts[317].pntx" 0;
setAttr "l_hand_geoShape.pnts[318].pntx" 0;
setAttr "l_hand_geoShape.pnts[319].pntx" 0;
setAttr "l_hand_geoShape.pnts[320].pntx" 0;
setAttr "l_hand_geoShape.pnts[321].pntx" 0;
setAttr "l_hand_geoShape.pnts[322].pntx" 0;
setAttr "l_hand_geoShape.pnts[323].pntx" 0;
setAttr "l_hand_geoShape.pnts[324].pntx" 0;
setAttr "l_hand_geoShape.pnts[325].pntx" 0;
setAttr "l_hand_geoShape.pnts[326].pntx" 0;
setAttr "l_hand_geoShape.pnts[327].pntx" 0;
setAttr "l_hand_geoShape.pnts[328].pntx" 0;
setAttr "l_hand_geoShape.pnts[329].pntx" 0;
setAttr "l_hand_geoShape.pnts[330].pntx" 0;
setAttr "l_hand_geoShape.pnts[331].pntx" 0;
setAttr "l_hand_geoShape.pnts[332].pntx" 0;
setAttr "l_hand_geoShape.pnts[333].pntx" 0;
setAttr "l_hand_geoShape.pnts[334].pntx" 0;
setAttr "l_hand_geoShape.pnts[335].pntx" 0;
setAttr "l_hand_geoShape.pnts[336].pntx" 0;
setAttr "l_hand_geoShape.pnts[337].pntx" 0;
setAttr "l_hand_geoShape.pnts[338].pntx" 0;
setAttr "l_hand_geoShape.pnts[339].pntx" 0;
setAttr "l_hand_geoShape.pnts[340].pntx" 0;
setAttr "l_hand_geoShape.pnts[341].pntx" 0;
setAttr "l_hand_geoShape.pnts[342].pntx" 0;
setAttr "l_hand_geoShape.pnts[343].pntx" 0;
setAttr "l_hand_geoShape.pnts[344].pntx" 0;
setAttr "l_hand_geoShape.pnts[345].pntx" 0;
setAttr "l_hand_geoShape.pnts[346].pntx" 0;
setAttr "l_hand_geoShape.pnts[347].pntx" 0;
setAttr "l_hand_geoShape.pnts[348].pntx" 0;
setAttr "l_hand_geoShape.pnts[349].pntx" 0;
setAttr "l_hand_geoShape.pnts[350].pntx" 0;
setAttr "l_hand_geoShape.pnts[351].pntx" 0;
setAttr "l_hand_geoShape.pnts[352].pntx" 0;
setAttr "l_hand_geoShape.pnts[353].pntx" 0;
setAttr "l_hand_geoShape.pnts[354].pntx" 0;
setAttr "l_hand_geoShape.pnts[355].pntx" 0;
setAttr "l_hand_geoShape.pnts[356].pntx" 0;
setAttr "l_hand_geoShape.pnts[357].pntx" 0;
setAttr "l_hand_geoShape.pnts[358].pntx" 0;
setAttr "l_hand_geoShape.pnts[359].pntx" 0;
setAttr "l_hand_geoShape.pnts[360].pntx" 0;
setAttr "l_hand_geoShape.pnts[361].pntx" 0;
setAttr "l_hand_geoShape.pnts[362].pntx" 0;
setAttr "l_hand_geoShape.pnts[363].pntx" 0;
setAttr "l_hand_geoShape.pnts[364].pntx" 0;
setAttr "l_hand_geoShape.pnts[365].pntx" 0;
setAttr "l_hand_geoShape.pnts[366].pntx" 0;
setAttr "l_hand_geoShape.pnts[367].pntx" 0;
setAttr "l_hand_geoShape.pnts[368].pntx" 0;
setAttr "l_hand_geoShape.pnts[369].pntx" 0;
setAttr "l_hand_geoShape.pnts[370].pntx" 0;
setAttr "l_hand_geoShape.pnts[371].pntx" 0;
setAttr "l_hand_geoShape.pnts[372].pntx" 0;
setAttr "l_hand_geoShape.pnts[373].pntx" 0;
setAttr "l_hand_geoShape.pnts[374].pntx" 0;
setAttr "l_hand_geoShape.pnts[375].pntx" 0;
setAttr "l_hand_geoShape.pnts[376].pntx" 0;
setAttr "l_hand_geoShape.pnts[377].pntx" 0;
setAttr "l_hand_geoShape.pnts[378].pntx" 0;
setAttr "l_hand_geoShape.pnts[379].pntx" 0;
setAttr "l_hand_geoShape.pnts[380].pntx" 0;
setAttr "l_hand_geoShape.pnts[381].pntx" 0;
setAttr "l_hand_geoShape.pnts[382].pntx" 0;
setAttr "l_hand_geoShape.pnts[383].pntx" 0;
setAttr "l_hand_geoShape.pnts[384].pntx" 0;
setAttr "l_hand_geoShape.pnts[385].pntx" 0;
setAttr "l_hand_geoShape.pnts[386].pntx" 0;
setAttr "l_hand_geoShape.pnts[387].pntx" 0;
setAttr "l_hand_geoShape.pnts[388].pntx" 0;
setAttr "l_hand_geoShape.pnts[389].pntx" 0;
setAttr "l_hand_geoShape.pnts[390].pntx" 0;
setAttr "l_hand_geoShape.pnts[391].pntx" 0;
setAttr "l_hand_geoShape.pnts[392].pntx" 0;
setAttr "l_hand_geoShape.pnts[393].pntx" 0;
setAttr "l_hand_geoShape.pnts[394].pntx" 0;
setAttr "l_hand_geoShape.pnts[395].pntx" 0;
setAttr "l_hand_geoShape.pnts[396].pntx" 0;
setAttr "l_hand_geoShape.pnts[397].pntx" 0;
setAttr "l_hand_geoShape.pnts[398].pntx" 0;
setAttr "l_hand_geoShape.pnts[399].pntx" 0;
setAttr "l_hand_geoShape.pnts[400].pntx" 0;
setAttr "l_hand_geoShape.pnts[401].pntx" 0;
setAttr "l_hand_geoShape.pnts[402].pntx" 0;
setAttr "l_hand_geoShape.pnts[403].pntx" 0;
setAttr "l_hand_geoShape.pnts[404].pntx" 0;
setAttr "l_hand_geoShape.pnts[405].pntx" 0;
setAttr "l_hand_geoShape.pnts[406].pntx" 0;
setAttr "l_hand_geoShape.pnts[407].pntx" 0;
setAttr "l_hand_geoShape.pnts[408].pntx" 0;
setAttr "l_hand_geoShape.pnts[409].pntx" 0;
setAttr "l_hand_geoShape.pnts[410].pntx" 0;
setAttr "l_hand_geoShape.pnts[411].pntx" 0;
setAttr "l_hand_geoShape.pnts[412].pntx" 0;
setAttr "l_hand_geoShape.pnts[413].pntx" 0;
setAttr "l_hand_geoShape.pnts[414].pntx" 0;
setAttr "l_hand_geoShape.pnts[415].pntx" 0;
setAttr "l_hand_geoShape.pnts[416].pntx" 0;
setAttr "l_hand_geoShape.pnts[417].pntx" 0;
setAttr "l_hand_geoShape.pnts[418].pntx" 0;
setAttr "l_hand_geoShape.pnts[419].pntx" 0;
setAttr "l_hand_geoShape.pnts[420].pntx" 0;
setAttr "l_hand_geoShape.pnts[421].pntx" 0;
setAttr "l_hand_geoShape.pnts[422].pntx" 0;
setAttr "l_hand_geoShape.pnts[423].pntx" 0;
setAttr "l_hand_geoShape.pnts[424].pntx" 0;
setAttr "l_hand_geoShape.pnts[425].pntx" 0;
setAttr "l_hand_geoShape.pnts[426].pntx" 0;
setAttr "l_hand_geoShape.pnts[427].pntx" 0;
setAttr "l_hand_geoShape.pnts[428].pntx" 0;
setAttr "l_hand_geoShape.pnts[429].pntx" 0;
setAttr "l_hand_geoShape.pnts[430].pntx" 0;
setAttr "l_hand_geoShape.pnts[431].pntx" 0;
setAttr "l_hand_geoShape.pnts[432].pntx" 0;
setAttr "l_hand_geoShape.pnts[433].pntx" 0;
setAttr "l_hand_geoShape.pnts[434].pntx" 0;
setAttr "l_hand_geoShape.pnts[435].pntx" 0;
setAttr "l_hand_geoShape.pnts[436].pntx" 0;
setAttr "l_hand_geoShape.pnts[437].pntx" 0;
setAttr "l_hand_geoShape.pnts[438].pntx" 0;
setAttr "l_hand_geoShape.pnts[439].pntx" 0;
setAttr "l_hand_geoShape.pnts[440].pntx" 0;
setAttr "l_hand_geoShape.pnts[441].pntx" 0;
setAttr "l_hand_geoShape.pnts[442].pntx" 0;
setAttr "l_hand_geoShape.pnts[443].pntx" 0;
setAttr "l_hand_geoShape.pnts[444].pntx" 0;
setAttr "l_hand_geoShape.pnts[445].pntx" 0;
setAttr "l_hand_geoShape.pnts[446].pntx" 0;
setAttr "l_hand_geoShape.pnts[447].pntx" 0;
setAttr "l_hand_geoShape.pnts[448].pntx" 0;
setAttr "l_hand_geoShape.pnts[449].pntx" 0;
setAttr "l_hand_geoShape.pnts[450].pntx" 0;
setAttr "l_hand_geoShape.pnts[451].pntx" 0;
setAttr "l_hand_geoShape.pnts[452].pntx" 0;
setAttr "l_hand_geoShape.pnts[453].pntx" 0;
setAttr "l_hand_geoShape.pnts[454].pntx" 0;
setAttr "l_hand_geoShape.pnts[455].pntx" 0;
setAttr "l_hand_geoShape.pnts[456].pntx" 0;
setAttr "l_hand_geoShape.pnts[457].pntx" 0;
setAttr "l_hand_geoShape.pnts[458].pntx" 0;
setAttr "l_hand_geoShape.pnts[459].pntx" 0;
setAttr "l_hand_geoShape.pnts[460].pntx" 0;
setAttr "l_hand_geoShape.pnts[461].pntx" 0;
setAttr "l_hand_geoShape.pnts[462].pntx" 0;
setAttr "l_hand_geoShape.pnts[463].pntx" 0;
setAttr "l_hand_geoShape.pnts[464].pntx" 0;
setAttr "l_hand_geoShape.pnts[465].pntx" 0;
setAttr "l_hand_geoShape.pnts[466].pntx" 0;
setAttr "l_hand_geoShape.pnts[467].pntx" 0;
setAttr "l_hand_geoShape.pnts[468].pntx" 0;
setAttr "l_hand_geoShape.pnts[469].pntx" 0;
setAttr "l_hand_geoShape.pnts[470].pntx" 0;
setAttr "l_hand_geoShape.pnts[471].pntx" 0;
setAttr "l_hand_geoShape.pnts[472].pntx" 0;
setAttr "l_hand_geoShape.pnts[473].pntx" 0;
setAttr "l_hand_geoShape.pnts[474].pntx" 0;
setAttr "l_hand_geoShape.pnts[475].pntx" 0;
setAttr "l_hand_geoShape.pnts[476].pntx" 0;
setAttr "l_hand_geoShape.pnts[477].pntx" 0;
setAttr "l_hand_geoShape.pnts[478].pntx" 0;
setAttr "l_hand_geoShape.pnts[479].pntx" 0;
setAttr "l_hand_geoShape.pnts[480].pntx" 0;
setAttr "l_hand_geoShape.pnts[481].pntx" 0;
setAttr "l_hand_geoShape.pnts[482].pntx" 0;
setAttr "l_hand_geoShape.pnts[483].pntx" 0;
setAttr "l_hand_geoShape.pnts[484].pntx" 0;
setAttr "l_hand_geoShape.pnts[485].pntx" 0;
setAttr "l_hand_geoShape.pnts[486].pntx" 0;
setAttr "l_hand_geoShape.pnts[487].pntx" 0;
setAttr "l_hand_geoShape.pnts[488].pntx" 0;
setAttr "l_hand_geoShape.pnts[489].pntx" 0;
setAttr "l_hand_geoShape.pnts[490].pntx" 0;
setAttr "l_hand_geoShape.pnts[491].pntx" 0;
setAttr "l_hand_geoShape.pnts[492].pntx" 0;
setAttr "l_hand_geoShape.pnts[493].pntx" 0;
setAttr "l_hand_geoShape.pnts[494].pntx" 0;
setAttr "l_hand_geoShape.pnts[495].pntx" 0;
setAttr "l_hand_geoShape.pnts[496].pntx" 0;
setAttr "l_hand_geoShape.pnts[497].pntx" 0;
setAttr "l_hand_geoShape.pnts[498].pntx" 0;
setAttr "l_hand_geoShape.pnts[499].pntx" 0;
setAttr "l_hand_geoShape.pnts[500].pntx" 0;
setAttr "l_hand_geoShape.pnts[501].pntx" 0;
setAttr "l_hand_geoShape.pnts[502].pntx" 0;
setAttr "l_hand_geoShape.pnts[503].pntx" 0;
setAttr "l_hand_geoShape.pnts[504].pntx" 0;
setAttr "l_hand_geoShape.pnts[505].pntx" 0;
setAttr "l_hand_geoShape.pnts[506].pntx" 0;
setAttr "l_hand_geoShape.pnts[507].pntx" 0;
setAttr "l_hand_geoShape.pnts[508].pntx" 0;
setAttr "l_hand_geoShape.pnts[509].pntx" 0;
setAttr "l_hand_geoShape.pnts[510].pntx" 0;
setAttr "l_hand_geoShape.pnts[511].pntx" 0;
setAttr "l_hand_geoShape.pnts[512].pntx" 0;
setAttr "l_hand_geoShape.pnts[513].pntx" 0;
setAttr "l_hand_geoShape.pnts[514].pntx" 0;
setAttr "l_hand_geoShape.pnts[515].pntx" 0;
setAttr "l_hand_geoShape.pnts[516].pntx" 0;
setAttr "l_hand_geoShape.pnts[517].pntx" 0;
setAttr "l_hand_geoShape.pnts[518].pntx" 0;
setAttr "l_hand_geoShape.pnts[519].pntx" 0;
setAttr "l_hand_geoShape.pnts[520].pntx" 0;
setAttr "l_hand_geoShape.pnts[521].pntx" 0;
setAttr "l_hand_geoShape.pnts[522].pntx" 0;
setAttr "l_hand_geoShape.pnts[523].pntx" 0;
setAttr "l_hand_geoShape.pnts[524].pntx" 0;
setAttr "l_hand_geoShape.pnts[525].pntx" 0;
setAttr "l_hand_geoShape.pnts[526].pntx" 0;
setAttr "l_hand_geoShape.pnts[527].pntx" 0;
setAttr "l_hand_geoShape.pnts[528].pntx" 0;
setAttr "l_hand_geoShape.pnts[529].pntx" 0;
setAttr "l_hand_geoShape.pnts[530].pntx" 0;
setAttr "l_hand_geoShape.pnts[531].pntx" 0;
setAttr "l_hand_geoShape.pnts[532].pntx" 0;
setAttr "l_hand_geoShape.pnts[533].pntx" 0;
setAttr "l_hand_geoShape.pnts[534].pntx" 0;
setAttr "l_hand_geoShape.pnts[535].pntx" 0;
setAttr "l_hand_geoShape.pnts[536].pntx" 0;
setAttr "l_hand_geoShape.pnts[537].pntx" 0;
setAttr "l_hand_geoShape.pnts[538].pntx" 0;
setAttr "l_hand_geoShape.pnts[539].pntx" 0;
setAttr "l_hand_geoShape.pnts[540].pntx" 0;
setAttr "l_hand_geoShape.pnts[541].pntx" 0;
setAttr "l_hand_geoShape.pnts[542].pntx" 0;
setAttr "l_hand_geoShape.pnts[543].pntx" 0;
setAttr "l_hand_geoShape.pnts[544].pntx" 0;
setAttr "l_hand_geoShape.pnts[545].pntx" 0;
setAttr "l_hand_geoShape.pnts[546].pntx" 0;
setAttr "l_hand_geoShape.pnts[547].pntx" 0;
setAttr "l_hand_geoShape.pnts[548].pntx" 0;
setAttr "l_hand_geoShape.pnts[549].pntx" 0;
setAttr "l_hand_geoShape.pnts[550].pntx" 0;
setAttr "l_hand_geoShape.pnts[551].pntx" 0;
setAttr "l_hand_geoShape.pnts[552].pntx" 0;
setAttr "l_hand_geoShape.pnts[553].pntx" 0;
setAttr "l_hand_geoShape.pnts[554].pntx" 0;
setAttr "l_hand_geoShape.pnts[555].pntx" 0;
setAttr "l_hand_geoShape.pnts[556].pntx" 0;
setAttr "l_hand_geoShape.pnts[557].pntx" 0;
setAttr "l_hand_geoShape.pnts[558].pntx" 0;
setAttr "l_hand_geoShape.pnts[559].pntx" 0;
setAttr "l_hand_geoShape.pnts[560].pntx" 0;
setAttr "l_hand_geoShape.pnts[561].pntx" 0;
setAttr "l_hand_geoShape.pnts[562].pntx" 0;
setAttr "l_hand_geoShape.pnts[563].pntx" 0;
setAttr "l_hand_geoShape.pnts[564].pntx" 0;
setAttr "l_hand_geoShape.pnts[565].pntx" 0;
setAttr "l_hand_geoShape.pnts[566].pntx" 0;
setAttr "l_hand_geoShape.pnts[567].pntx" 0;
setAttr "l_hand_geoShape.pnts[568].pntx" 0;
setAttr "l_hand_geoShape.pnts[569].pntx" 0;
setAttr "l_hand_geoShape.pnts[570].pntx" 0;
setAttr "l_hand_geoShape.pnts[571].pntx" 0;
setAttr "l_hand_geoShape.pnts[572].pntx" 0;
setAttr "l_hand_geoShape.pnts[573].pntx" 0;
setAttr "l_hand_geoShape.pnts[574].pntx" 0;
setAttr "l_hand_geoShape.pnts[575].pntx" 0;
setAttr "l_hand_geoShape.pnts[576].pntx" 0;
setAttr "l_hand_geoShape.pnts[577].pntx" 0;
setAttr "l_hand_geoShape.pnts[578].pntx" 0;
setAttr "l_hand_geoShape.pnts[579].pntx" 0;
setAttr "l_hand_geoShape.pnts[580].pntx" 0;
setAttr "l_hand_geoShape.pnts[581].pntx" 0;
setAttr "l_hand_geoShape.pnts[582].pntx" 0;
setAttr "l_hand_geoShape.pnts[583].pntx" 0;
setAttr "l_hand_geoShape.pnts[584].pntx" 0;
setAttr "l_hand_geoShape.pnts[585].pntx" 0;
setAttr "l_hand_geoShape.pnts[586].pntx" 0;
setAttr "l_hand_geoShape.pnts[587].pntx" 0;
setAttr "l_hand_geoShape.pnts[588].pntx" 0;
setAttr "l_hand_geoShape.pnts[589].pntx" 0;
setAttr "l_hand_geoShape.pnts[590].pntx" 0;
setAttr "l_hand_geoShape.pnts[591].pntx" 0;
setAttr "l_hand_geoShape.pnts[592].pntx" 0;
setAttr "l_hand_geoShape.pnts[593].pntx" 0;
setAttr "l_hand_geoShape.pnts[594].pntx" 0;
setAttr "l_hand_geoShape.pnts[595].pntx" 0;
setAttr "l_hand_geoShape.pnts[596].pntx" 0;
setAttr "l_hand_geoShape.pnts[597].pntx" 0;
setAttr "l_hand_geoShape.pnts[598].pntx" 0;
setAttr "l_hand_geoShape.pnts[599].pntx" 0;
setAttr "l_hand_geoShape.pnts[600].pntx" 0;
setAttr "l_hand_geoShape.pnts[601].pntx" 0;
setAttr "l_hand_geoShape.pnts[602].pntx" 0;
setAttr "l_hand_geoShape.pnts[603].pntx" 0;
setAttr "l_hand_geoShape.pnts[604].pntx" 0;
setAttr "l_hand_geoShape.pnts[605].pntx" 0;
setAttr "l_hand_geoShape.pnts[606].pntx" 0;
setAttr "l_hand_geoShape.pnts[607].pntx" 0;
setAttr "l_hand_geoShape.pnts[608].pntx" 0;
setAttr "l_hand_geoShape.pnts[609].pntx" 0;
setAttr "l_hand_geoShape.pnts[610].pntx" 0;
setAttr "l_hand_geoShape.pnts[611].pntx" 0;
setAttr "l_hand_geoShape.pnts[612].pntx" 0;
setAttr "l_hand_geoShape.pnts[613].pntx" 0;
setAttr "l_hand_geoShape.pnts[614].pntx" 0;
setAttr "l_hand_geoShape.pnts[615].pntx" 0;
setAttr "l_hand_geoShape.pnts[616].pntx" 0;
setAttr "l_hand_geoShape.pnts[617].pntx" 0;
setAttr "l_hand_geoShape.pnts[618].pntx" 0;
setAttr "l_hand_geoShape.pnts[619].pntx" 0;
setAttr "l_hand_geoShape.pnts[620].pntx" 0;
setAttr "l_hand_geoShape.pnts[621].pntx" 0;
setAttr "l_hand_geoShape.pnts[622].pntx" 0;
setAttr "l_hand_geoShape.pnts[623].pntx" 0;
setAttr "l_hand_geoShape.pnts[624].pntx" 0;
setAttr "l_hand_geoShape.pnts[625].pntx" 0;
setAttr "l_hand_geoShape.pnts[626].pntx" 0;
setAttr "l_hand_geoShape.pnts[627].pntx" 0;
setAttr "l_hand_geoShape.pnts[628].pntx" 0;
setAttr "l_hand_geoShape.pnts[629].pntx" 0;
setAttr "l_hand_geoShape.pnts[630].pntx" 0;
setAttr "l_hand_geoShape.pnts[631].pntx" 0;
setAttr "l_hand_geoShape.pnts[632].pntx" 0;
setAttr "l_hand_geoShape.pnts[633].pntx" 0;
setAttr "l_hand_geoShape.pnts[634].pntx" 0;
setAttr "l_hand_geoShape.pnts[635].pntx" 0;
setAttr "l_hand_geoShape.pnts[636].pntx" 0;
setAttr "l_hand_geoShape.pnts[637].pntx" 0;
setAttr "l_hand_geoShape.pnts[638].pntx" 0;
setAttr "l_hand_geoShape.pnts[639].pntx" 0;
setAttr "l_hand_geoShape.pnts[640].pntx" 0;
setAttr "l_hand_geoShape.pnts[641].pntx" 0;
setAttr "l_hand_geoShape.pnts[642].pntx" 0;
setAttr "l_hand_geoShape.pnts[643].pntx" 0;
setAttr "l_hand_geoShape.pnts[644].pntx" 0;
setAttr "l_hand_geoShape.pnts[645].pntx" 0;
setAttr "l_hand_geoShape.pnts[646].pntx" 0;
setAttr "l_hand_geoShape.pnts[647].pntx" 0;
setAttr "l_hand_geoShape.pnts[648].pntx" 0;
setAttr "l_hand_geoShape.pnts[649].pntx" 0;
setAttr "l_hand_geoShape.pnts[650].pntx" 0;
setAttr "l_hand_geoShape.pnts[651].pntx" 0;
setAttr "l_hand_geoShape.pnts[652].pntx" 0;
setAttr "l_hand_geoShape.pnts[653].pntx" 0;
setAttr "l_hand_geoShape.pnts[654].pntx" 0;
setAttr "l_hand_geoShape.pnts[655].pntx" 0;
setAttr "l_hand_geoShape.pnts[656].pntx" 0;
setAttr "l_hand_geoShape.pnts[657].pntx" 0;
setAttr "l_hand_geoShape.pnts[658].pntx" 0;
setAttr "l_hand_geoShape.pnts[659].pntx" 0;
setAttr "l_hand_geoShape.pnts[660].pntx" 0;
setAttr "l_hand_geoShape.pnts[661].pntx" 0;
setAttr "l_hand_geoShape.pnts[662].pntx" 0;
setAttr "l_hand_geoShape.pnts[663].pntx" 0;
setAttr "l_hand_geoShape.pnts[664].pntx" 0;
setAttr "l_hand_geoShape.pnts[665].pntx" 0;
setAttr "l_hand_geoShape.pnts[666].pntx" 0;
setAttr "l_hand_geoShape.pnts[667].pntx" 0;
setAttr "l_hand_geoShape.pnts[668].pntx" 0;
setAttr "l_hand_geoShape.pnts[669].pntx" 0;
setAttr "l_hand_geoShape.pnts[670].pntx" 0;
setAttr "l_hand_geoShape.pnts[671].pntx" 0;
setAttr "l_hand_geoShape.pnts[672].pntx" 0;
setAttr "l_hand_geoShape.pnts[673].pntx" 0;
setAttr "l_hand_geoShape.pnts[674].pntx" 0;
setAttr "l_hand_geoShape.pnts[675].pntx" 0;
setAttr "l_hand_geoShape.pnts[676].pntx" 0;
setAttr "l_hand_geoShape.pnts[677].pntx" 0;
setAttr "l_hand_geoShape.pnts[678].pntx" 0;
setAttr "l_hand_geoShape.pnts[679].pntx" 0;
setAttr "l_hand_geoShape.pnts[680].pntx" 0;
setAttr "l_hand_geoShape.pnts[681].pntx" 0;
setAttr "l_hand_geoShape.pnts[682].pntx" 0;
setAttr "l_hand_geoShape.pnts[683].pntx" 0;
setAttr "l_hand_geoShape.pnts[684].pntx" 0;
setAttr "l_hand_geoShape.pnts[685].pntx" 0;
setAttr "l_hand_geoShape.pnts[686].pntx" 0;
setAttr "l_hand_geoShape.pnts[687].pntx" 0;
setAttr "l_hand_geoShape.pnts[688].pntx" 0;
setAttr "l_hand_geoShape.pnts[689].pntx" 0;
setAttr "l_hand_geoShape.pnts[690].pntx" 0;
setAttr "l_hand_geoShape.pnts[691].pntx" 0;
setAttr "l_hand_geoShape.pnts[692].pntx" 0;
setAttr "l_hand_geoShape.pnts[693].pntx" 0;
setAttr "l_hand_geoShape.pnts[694].pntx" 0;
setAttr "l_hand_geoShape.pnts[695].pntx" 0;
setAttr "l_hand_geoShape.pnts[696].pntx" 0;
setAttr "l_hand_geoShape.pnts[697].pntx" 0;
setAttr "l_hand_geoShape.pnts[698].pntx" 0;
setAttr "l_hand_geoShape.pnts[699].pntx" 0;
setAttr "l_hand_geoShape.pnts[700].pntx" 0;
setAttr "l_hand_geoShape.pnts[701].pntx" 0;
setAttr "l_hand_geoShape.pnts[702].pntx" 0;
setAttr "l_hand_geoShape.pnts[703].pntx" 0;
setAttr "l_hand_geoShape.pnts[704].pntx" 0;
setAttr "l_hand_geoShape.pnts[705].pntx" 0;
setAttr "l_hand_geoShape.pnts[706].pntx" 0;
setAttr "l_hand_geoShape.pnts[707].pntx" 0;
setAttr "l_hand_geoShape.pnts[708].pntx" 0;
setAttr "l_hand_geoShape.pnts[709].pntx" 0;
setAttr "l_hand_geoShape.pnts[710].pntx" 0;
setAttr "l_hand_geoShape.pnts[711].pntx" 0;
setAttr "l_hand_geoShape.pnts[712].pntx" 0;
setAttr "l_hand_geoShape.pnts[713].pntx" 0;
setAttr "l_hand_geoShape.pnts[714].pntx" 0;
setAttr "l_hand_geoShape.pnts[715].pntx" 0;
setAttr "l_hand_geoShape.pnts[716].pntx" 0;
setAttr "l_hand_geoShape.pnts[717].pntx" 0;
setAttr "l_hand_geoShape.pnts[718].pntx" 0;
setAttr "l_hand_geoShape.pnts[719].pntx" 0;
setAttr "l_hand_geoShape.pnts[720].pntx" 0;
setAttr "l_hand_geoShape.pnts[721].pntx" 0;
setAttr "l_hand_geoShape.pnts[722].pntx" 0;
setAttr "l_hand_geoShape.pnts[723].pntx" 0;
setAttr "l_hand_geoShape.pnts[724].pntx" 0;
setAttr "l_hand_geoShape.pnts[725].pntx" 0;
setAttr "l_hand_geoShape.pnts[726].pntx" 0;
setAttr "l_hand_geoShape.pnts[727].pntx" 0;
setAttr "l_hand_geoShape.pnts[728].pntx" 0;
setAttr "l_hand_geoShape.pnts[729].pntx" 0;
setAttr "l_hand_geoShape.pnts[730].pntx" 0;
setAttr "l_hand_geoShape.pnts[731].pntx" 0;
setAttr "l_hand_geoShape.pnts[732].pntx" 0;
setAttr "l_hand_geoShape.pnts[733].pntx" 0;
setAttr "l_hand_geoShape.pnts[734].pntx" 0;
setAttr "l_hand_geoShape.pnts[735].pntx" 0;
setAttr "l_hand_geoShape.pnts[736].pntx" 0;
setAttr "l_hand_geoShape.pnts[737].pntx" 0;
setAttr "l_hand_geoShape.pnts[738].pntx" 0;
setAttr "l_hand_geoShape.pnts[739].pntx" 0;
setAttr "l_hand_geoShape.pnts[740].pntx" 0;
setAttr "l_hand_geoShape.pnts[741].pntx" 0;
setAttr "l_hand_geoShape.pnts[742].pntx" 0;
setAttr "l_hand_geoShape.pnts[743].pntx" 0;
setAttr "l_hand_geoShape.pnts[744].pntx" 0;
setAttr "l_hand_geoShape.pnts[745].pntx" 0;
setAttr "l_hand_geoShape.pnts[746].pntx" 0;
setAttr "l_hand_geoShape.pnts[747].pntx" 0;
setAttr "l_hand_geoShape.pnts[748].pntx" 0;
setAttr "l_hand_geoShape.pnts[749].pntx" 0;
setAttr "l_hand_geoShape.pnts[750].pntx" 0;
setAttr "l_hand_geoShape.pnts[751].pntx" 0;
setAttr "l_hand_geoShape.pnts[752].pntx" 0;
setAttr "l_hand_geoShape.pnts[753].pntx" 0;
setAttr "l_hand_geoShape.pnts[754].pntx" 0;
setAttr "l_hand_geoShape.pnts[755].pntx" 0;
setAttr "l_hand_geoShape.pnts[756].pntx" 0;
setAttr "l_hand_geoShape.pnts[757].pntx" 0;
setAttr "l_hand_geoShape.pnts[758].pntx" 0;
setAttr "l_hand_geoShape.pnts[759].pntx" 0;
setAttr "l_hand_geoShape.pnts[760].pntx" 0;
setAttr "l_hand_geoShape.pnts[761].pntx" 0;
setAttr "l_hand_geoShape.pnts[762].pntx" 0;
setAttr "l_hand_geoShape.pnts[763].pntx" 0;
setAttr "l_hand_geoShape.pnts[764].pntx" 0;
setAttr "l_hand_geoShape.pnts[765].pntx" 0;
setAttr "l_hand_geoShape.pnts[766].pntx" 0;
setAttr "l_hand_geoShape.pnts[0].pntx" 0;
// Undo: setAttr "l_hand_geoShape.pnts[0].pntx" 0;
// Undo: setAttr "l_hand_geoShape.pnts[0].pntx" 0;
setAttr "l_hand_geoShape.pnts[1].pntx" 0;
setAttr "l_hand_geoShape.pnts[2].pntx" 0;
setAttr "l_hand_geoShape.pnts[3].pntx" 0;
setAttr "l_hand_geoShape.pnts[4].pntx" 0;
setAttr "l_hand_geoShape.pnts[5].pntx" 0;
setAttr "l_hand_geoShape.pnts[6].pntx" 0;
setAttr "l_hand_geoShape.pnts[7].pntx" 0;
setAttr "l_hand_geoShape.pnts[8].pntx" 0;
setAttr "l_hand_geoShape.pnts[9].pntx" 0;
setAttr "l_hand_geoShape.pnts[10].pntx" 0;
setAttr "l_hand_geoShape.pnts[11].pntx" 0;
setAttr "l_hand_geoShape.pnts[12].pntx" 0;
setAttr "l_hand_geoShape.pnts[13].pntx" 0;
setAttr "l_hand_geoShape.pnts[14].pntx" 0;
setAttr "l_hand_geoShape.pnts[15].pntx" 0;
setAttr "l_hand_geoShape.pnts[16].pntx" 0;
setAttr "l_hand_geoShape.pnts[17].pntx" 0;
setAttr "l_hand_geoShape.pnts[18].pntx" 0;
setAttr "l_hand_geoShape.pnts[19].pntx" 0;
setAttr "l_hand_geoShape.pnts[20].pntx" 0;
setAttr "l_hand_geoShape.pnts[21].pntx" 0;
setAttr "l_hand_geoShape.pnts[22].pntx" 0;
setAttr "l_hand_geoShape.pnts[23].pntx" 0;
setAttr "l_hand_geoShape.pnts[24].pntx" 0;
setAttr "l_hand_geoShape.pnts[25].pntx" 0;
setAttr "l_hand_geoShape.pnts[26].pntx" 0;
setAttr "l_hand_geoShape.pnts[27].pntx" 0;
setAttr "l_hand_geoShape.pnts[28].pntx" 0;
setAttr "l_hand_geoShape.pnts[29].pntx" 0;
setAttr "l_hand_geoShape.pnts[30].pntx" 0;
setAttr "l_hand_geoShape.pnts[31].pntx" 0;
setAttr "l_hand_geoShape.pnts[32].pntx" 0;
setAttr "l_hand_geoShape.pnts[33].pntx" 0;
setAttr "l_hand_geoShape.pnts[34].pntx" 0;
setAttr "l_hand_geoShape.pnts[35].pntx" 0;
setAttr "l_hand_geoShape.pnts[36].pntx" 0;
setAttr "l_hand_geoShape.pnts[37].pntx" 0;
setAttr "l_hand_geoShape.pnts[38].pntx" 0;
setAttr "l_hand_geoShape.pnts[39].pntx" 0;
setAttr "l_hand_geoShape.pnts[40].pntx" 0;
setAttr "l_hand_geoShape.pnts[41].pntx" 0;
setAttr "l_hand_geoShape.pnts[42].pntx" 0;
setAttr "l_hand_geoShape.pnts[43].pntx" 0;
setAttr "l_hand_geoShape.pnts[44].pntx" 0;
setAttr "l_hand_geoShape.pnts[45].pntx" 0;
setAttr "l_hand_geoShape.pnts[46].pntx" 0;
setAttr "l_hand_geoShape.pnts[47].pntx" 0;
setAttr "l_hand_geoShape.pnts[48].pntx" 0;
setAttr "l_hand_geoShape.pnts[49].pntx" 0;
setAttr "l_hand_geoShape.pnts[50].pntx" 0;
setAttr "l_hand_geoShape.pnts[51].pntx" 0;
setAttr "l_hand_geoShape.pnts[52].pntx" 0;
setAttr "l_hand_geoShape.pnts[53].pntx" 0;
setAttr "l_hand_geoShape.pnts[54].pntx" 0;
setAttr "l_hand_geoShape.pnts[55].pntx" 0;
setAttr "l_hand_geoShape.pnts[56].pntx" 0;
setAttr "l_hand_geoShape.pnts[57].pntx" 0;
setAttr "l_hand_geoShape.pnts[58].pntx" 0;
setAttr "l_hand_geoShape.pnts[59].pntx" 0;
setAttr "l_hand_geoShape.pnts[60].pntx" 0;
setAttr "l_hand_geoShape.pnts[61].pntx" 0;
setAttr "l_hand_geoShape.pnts[62].pntx" 0;
setAttr "l_hand_geoShape.pnts[63].pntx" 0;
setAttr "l_hand_geoShape.pnts[64].pntx" 0;
setAttr "l_hand_geoShape.pnts[65].pntx" 0;
setAttr "l_hand_geoShape.pnts[66].pntx" 0;
setAttr "l_hand_geoShape.pnts[67].pntx" 0;
setAttr "l_hand_geoShape.pnts[68].pntx" 0;
setAttr "l_hand_geoShape.pnts[69].pntx" 0;
setAttr "l_hand_geoShape.pnts[70].pntx" 0;
setAttr "l_hand_geoShape.pnts[71].pntx" 0;
setAttr "l_hand_geoShape.pnts[72].pntx" 0;
setAttr "l_hand_geoShape.pnts[73].pntx" 0;
setAttr "l_hand_geoShape.pnts[74].pntx" 0;
setAttr "l_hand_geoShape.pnts[75].pntx" 0;
setAttr "l_hand_geoShape.pnts[76].pntx" 0;
setAttr "l_hand_geoShape.pnts[77].pntx" 0;
setAttr "l_hand_geoShape.pnts[78].pntx" 0;
setAttr "l_hand_geoShape.pnts[79].pntx" 0;
setAttr "l_hand_geoShape.pnts[80].pntx" 0;
setAttr "l_hand_geoShape.pnts[81].pntx" 0;
setAttr "l_hand_geoShape.pnts[82].pntx" 0;
setAttr "l_hand_geoShape.pnts[83].pntx" 0;
setAttr "l_hand_geoShape.pnts[84].pntx" 0;
setAttr "l_hand_geoShape.pnts[85].pntx" 0;
setAttr "l_hand_geoShape.pnts[86].pntx" 0;
setAttr "l_hand_geoShape.pnts[87].pntx" 0;
setAttr "l_hand_geoShape.pnts[88].pntx" 0;
setAttr "l_hand_geoShape.pnts[89].pntx" 0;
setAttr "l_hand_geoShape.pnts[90].pntx" 0;
setAttr "l_hand_geoShape.pnts[91].pntx" 0;
setAttr "l_hand_geoShape.pnts[92].pntx" 0;
setAttr "l_hand_geoShape.pnts[93].pntx" 0;
setAttr "l_hand_geoShape.pnts[94].pntx" 0;
setAttr "l_hand_geoShape.pnts[95].pntx" 0;
setAttr "l_hand_geoShape.pnts[96].pntx" 0;
setAttr "l_hand_geoShape.pnts[97].pntx" 0;
setAttr "l_hand_geoShape.pnts[98].pntx" 0;
setAttr "l_hand_geoShape.pnts[99].pntx" 0;
setAttr "l_hand_geoShape.pnts[100].pntx" 0;
setAttr "l_hand_geoShape.pnts[101].pntx" 0;
setAttr "l_hand_geoShape.pnts[102].pntx" 0;
setAttr "l_hand_geoShape.pnts[103].pntx" 0;
setAttr "l_hand_geoShape.pnts[104].pntx" 0;
setAttr "l_hand_geoShape.pnts[105].pntx" 0;
setAttr "l_hand_geoShape.pnts[106].pntx" 0;
setAttr "l_hand_geoShape.pnts[107].pntx" 0;
setAttr "l_hand_geoShape.pnts[108].pntx" 0;
setAttr "l_hand_geoShape.pnts[109].pntx" 0;
setAttr "l_hand_geoShape.pnts[110].pntx" 0;
setAttr "l_hand_geoShape.pnts[111].pntx" 0;
setAttr "l_hand_geoShape.pnts[112].pntx" 0;
setAttr "l_hand_geoShape.pnts[113].pntx" 0;
setAttr "l_hand_geoShape.pnts[114].pntx" 0;
setAttr "l_hand_geoShape.pnts[115].pntx" 0;
setAttr "l_hand_geoShape.pnts[116].pntx" 0;
setAttr "l_hand_geoShape.pnts[117].pntx" 0;
setAttr "l_hand_geoShape.pnts[118].pntx" 0;
setAttr "l_hand_geoShape.pnts[119].pntx" 0;
setAttr "l_hand_geoShape.pnts[120].pntx" 0;
setAttr "l_hand_geoShape.pnts[121].pntx" 0;
setAttr "l_hand_geoShape.pnts[122].pntx" 0;
setAttr "l_hand_geoShape.pnts[123].pntx" 0;
setAttr "l_hand_geoShape.pnts[124].pntx" 0;
setAttr "l_hand_geoShape.pnts[125].pntx" 0;
setAttr "l_hand_geoShape.pnts[126].pntx" 0;
setAttr "l_hand_geoShape.pnts[127].pntx" 0;
setAttr "l_hand_geoShape.pnts[128].pntx" 0;
setAttr "l_hand_geoShape.pnts[129].pntx" 0;
setAttr "l_hand_geoShape.pnts[130].pntx" 0;
setAttr "l_hand_geoShape.pnts[131].pntx" 0;
setAttr "l_hand_geoShape.pnts[132].pntx" 0;
setAttr "l_hand_geoShape.pnts[133].pntx" 0;
setAttr "l_hand_geoShape.pnts[134].pntx" 0;
setAttr "l_hand_geoShape.pnts[135].pntx" 0;
setAttr "l_hand_geoShape.pnts[136].pntx" 0;
setAttr "l_hand_geoShape.pnts[137].pntx" 0;
setAttr "l_hand_geoShape.pnts[138].pntx" 0;
setAttr "l_hand_geoShape.pnts[139].pntx" 0;
setAttr "l_hand_geoShape.pnts[140].pntx" 0;
setAttr "l_hand_geoShape.pnts[141].pntx" 0;
setAttr "l_hand_geoShape.pnts[142].pntx" 0;
setAttr "l_hand_geoShape.pnts[143].pntx" 0;
setAttr "l_hand_geoShape.pnts[144].pntx" 0;
setAttr "l_hand_geoShape.pnts[145].pntx" 0;
setAttr "l_hand_geoShape.pnts[146].pntx" 0;
setAttr "l_hand_geoShape.pnts[147].pntx" 0;
setAttr "l_hand_geoShape.pnts[148].pntx" 0;
setAttr "l_hand_geoShape.pnts[149].pntx" 0;
setAttr "l_hand_geoShape.pnts[150].pntx" 0;
setAttr "l_hand_geoShape.pnts[151].pntx" 0;
setAttr "l_hand_geoShape.pnts[152].pntx" 0;
setAttr "l_hand_geoShape.pnts[153].pntx" 0;
setAttr "l_hand_geoShape.pnts[154].pntx" 0;
setAttr "l_hand_geoShape.pnts[155].pntx" 0;
setAttr "l_hand_geoShape.pnts[156].pntx" 0;
setAttr "l_hand_geoShape.pnts[157].pntx" 0;
setAttr "l_hand_geoShape.pnts[158].pntx" 0;
setAttr "l_hand_geoShape.pnts[159].pntx" 0;
setAttr "l_hand_geoShape.pnts[160].pntx" 0;
setAttr "l_hand_geoShape.pnts[161].pntx" 0;
setAttr "l_hand_geoShape.pnts[162].pntx" 0;
setAttr "l_hand_geoShape.pnts[163].pntx" 0;
setAttr "l_hand_geoShape.pnts[164].pntx" 0;
setAttr "l_hand_geoShape.pnts[165].pntx" 0;
setAttr "l_hand_geoShape.pnts[166].pntx" 0;
setAttr "l_hand_geoShape.pnts[167].pntx" 0;
setAttr "l_hand_geoShape.pnts[168].pntx" 0;
setAttr "l_hand_geoShape.pnts[169].pntx" 0;
setAttr "l_hand_geoShape.pnts[170].pntx" 0;
setAttr "l_hand_geoShape.pnts[171].pntx" 0;
setAttr "l_hand_geoShape.pnts[172].pntx" 0;
setAttr "l_hand_geoShape.pnts[173].pntx" 0;
setAttr "l_hand_geoShape.pnts[174].pntx" 0;
setAttr "l_hand_geoShape.pnts[175].pntx" 0;
setAttr "l_hand_geoShape.pnts[176].pntx" 0;
setAttr "l_hand_geoShape.pnts[177].pntx" 0;
setAttr "l_hand_geoShape.pnts[178].pntx" 0;
setAttr "l_hand_geoShape.pnts[179].pntx" 0;
setAttr "l_hand_geoShape.pnts[180].pntx" 0;
setAttr "l_hand_geoShape.pnts[181].pntx" 0;
setAttr "l_hand_geoShape.pnts[182].pntx" 0;
setAttr "l_hand_geoShape.pnts[183].pntx" 0;
setAttr "l_hand_geoShape.pnts[184].pntx" 0;
setAttr "l_hand_geoShape.pnts[185].pntx" 0;
setAttr "l_hand_geoShape.pnts[186].pntx" 0;
setAttr "l_hand_geoShape.pnts[187].pntx" 0;
setAttr "l_hand_geoShape.pnts[188].pntx" 0;
setAttr "l_hand_geoShape.pnts[189].pntx" 0;
setAttr "l_hand_geoShape.pnts[190].pntx" 0;
setAttr "l_hand_geoShape.pnts[191].pntx" 0;
setAttr "l_hand_geoShape.pnts[192].pntx" 0;
setAttr "l_hand_geoShape.pnts[193].pntx" 0;
setAttr "l_hand_geoShape.pnts[194].pntx" 0;
setAttr "l_hand_geoShape.pnts[195].pntx" 0;
setAttr "l_hand_geoShape.pnts[196].pntx" 0;
setAttr "l_hand_geoShape.pnts[197].pntx" 0;
setAttr "l_hand_geoShape.pnts[198].pntx" 0;
setAttr "l_hand_geoShape.pnts[199].pntx" 0;
setAttr "l_hand_geoShape.pnts[200].pntx" 0;
setAttr "l_hand_geoShape.pnts[201].pntx" 0;
setAttr "l_hand_geoShape.pnts[202].pntx" 0;
setAttr "l_hand_geoShape.pnts[203].pntx" 0;
setAttr "l_hand_geoShape.pnts[204].pntx" 0;
setAttr "l_hand_geoShape.pnts[205].pntx" 0;
setAttr "l_hand_geoShape.pnts[206].pntx" 0;
setAttr "l_hand_geoShape.pnts[207].pntx" 0;
setAttr "l_hand_geoShape.pnts[208].pntx" 0;
setAttr "l_hand_geoShape.pnts[209].pntx" 0;
setAttr "l_hand_geoShape.pnts[210].pntx" 0;
setAttr "l_hand_geoShape.pnts[211].pntx" 0;
setAttr "l_hand_geoShape.pnts[212].pntx" 0;
setAttr "l_hand_geoShape.pnts[213].pntx" 0;
setAttr "l_hand_geoShape.pnts[214].pntx" 0;
setAttr "l_hand_geoShape.pnts[215].pntx" 0;
setAttr "l_hand_geoShape.pnts[216].pntx" 0;
setAttr "l_hand_geoShape.pnts[217].pntx" 0;
setAttr "l_hand_geoShape.pnts[218].pntx" 0;
setAttr "l_hand_geoShape.pnts[219].pntx" 0;
setAttr "l_hand_geoShape.pnts[220].pntx" 0;
setAttr "l_hand_geoShape.pnts[221].pntx" 0;
setAttr "l_hand_geoShape.pnts[222].pntx" 0;
setAttr "l_hand_geoShape.pnts[223].pntx" 0;
setAttr "l_hand_geoShape.pnts[224].pntx" 0;
setAttr "l_hand_geoShape.pnts[225].pntx" 0;
setAttr "l_hand_geoShape.pnts[226].pntx" 0;
setAttr "l_hand_geoShape.pnts[227].pntx" 0;
setAttr "l_hand_geoShape.pnts[228].pntx" 0;
setAttr "l_hand_geoShape.pnts[229].pntx" 0;
setAttr "l_hand_geoShape.pnts[230].pntx" 0;
setAttr "l_hand_geoShape.pnts[231].pntx" 0;
setAttr "l_hand_geoShape.pnts[232].pntx" 0;
setAttr "l_hand_geoShape.pnts[233].pntx" 0;
setAttr "l_hand_geoShape.pnts[234].pntx" 0;
setAttr "l_hand_geoShape.pnts[235].pntx" 0;
setAttr "l_hand_geoShape.pnts[236].pntx" 0;
setAttr "l_hand_geoShape.pnts[237].pntx" 0;
setAttr "l_hand_geoShape.pnts[238].pntx" 0;
setAttr "l_hand_geoShape.pnts[239].pntx" 0;
setAttr "l_hand_geoShape.pnts[240].pntx" 0;
setAttr "l_hand_geoShape.pnts[241].pntx" 0;
setAttr "l_hand_geoShape.pnts[242].pntx" 0;
setAttr "l_hand_geoShape.pnts[243].pntx" 0;
setAttr "l_hand_geoShape.pnts[244].pntx" 0;
setAttr "l_hand_geoShape.pnts[245].pntx" 0;
setAttr "l_hand_geoShape.pnts[246].pntx" 0;
setAttr "l_hand_geoShape.pnts[247].pntx" 0;
setAttr "l_hand_geoShape.pnts[248].pntx" 0;
setAttr "l_hand_geoShape.pnts[249].pntx" 0;
setAttr "l_hand_geoShape.pnts[250].pntx" 0;
setAttr "l_hand_geoShape.pnts[251].pntx" 0;
setAttr "l_hand_geoShape.pnts[252].pntx" 0;
setAttr "l_hand_geoShape.pnts[253].pntx" 0;
setAttr "l_hand_geoShape.pnts[254].pntx" 0;
setAttr "l_hand_geoShape.pnts[255].pntx" 0;
setAttr "l_hand_geoShape.pnts[256].pntx" 0;
setAttr "l_hand_geoShape.pnts[257].pntx" 0;
setAttr "l_hand_geoShape.pnts[258].pntx" 0;
setAttr "l_hand_geoShape.pnts[259].pntx" 0;
setAttr "l_hand_geoShape.pnts[260].pntx" 0;
setAttr "l_hand_geoShape.pnts[261].pntx" 0;
setAttr "l_hand_geoShape.pnts[262].pntx" 0;
setAttr "l_hand_geoShape.pnts[263].pntx" 0;
setAttr "l_hand_geoShape.pnts[264].pntx" 0;
setAttr "l_hand_geoShape.pnts[265].pntx" 0;
setAttr "l_hand_geoShape.pnts[266].pntx" 0;
setAttr "l_hand_geoShape.pnts[267].pntx" 0;
setAttr "l_hand_geoShape.pnts[268].pntx" 0;
setAttr "l_hand_geoShape.pnts[269].pntx" 0;
setAttr "l_hand_geoShape.pnts[270].pntx" 0;
setAttr "l_hand_geoShape.pnts[271].pntx" 0;
setAttr "l_hand_geoShape.pnts[272].pntx" 0;
setAttr "l_hand_geoShape.pnts[273].pntx" 0;
setAttr "l_hand_geoShape.pnts[274].pntx" 0;
setAttr "l_hand_geoShape.pnts[275].pntx" 0;
setAttr "l_hand_geoShape.pnts[276].pntx" 0;
setAttr "l_hand_geoShape.pnts[277].pntx" 0;
setAttr "l_hand_geoShape.pnts[278].pntx" 0;
setAttr "l_hand_geoShape.pnts[279].pntx" 0;
setAttr "l_hand_geoShape.pnts[280].pntx" 0;
setAttr "l_hand_geoShape.pnts[281].pntx" 0;
setAttr "l_hand_geoShape.pnts[282].pntx" 0;
setAttr "l_hand_geoShape.pnts[283].pntx" 0;
setAttr "l_hand_geoShape.pnts[284].pntx" 0;
setAttr "l_hand_geoShape.pnts[285].pntx" 0;
setAttr "l_hand_geoShape.pnts[286].pntx" 0;
setAttr "l_hand_geoShape.pnts[287].pntx" 0;
setAttr "l_hand_geoShape.pnts[288].pntx" 0;
setAttr "l_hand_geoShape.pnts[289].pntx" 0;
setAttr "l_hand_geoShape.pnts[290].pntx" 0;
setAttr "l_hand_geoShape.pnts[291].pntx" 0;
setAttr "l_hand_geoShape.pnts[292].pntx" 0;
setAttr "l_hand_geoShape.pnts[293].pntx" 0;
setAttr "l_hand_geoShape.pnts[294].pntx" 0;
setAttr "l_hand_geoShape.pnts[295].pntx" 0;
setAttr "l_hand_geoShape.pnts[296].pntx" 0;
setAttr "l_hand_geoShape.pnts[297].pntx" 0;
setAttr "l_hand_geoShape.pnts[298].pntx" 0;
setAttr "l_hand_geoShape.pnts[299].pntx" 0;
setAttr "l_hand_geoShape.pnts[300].pntx" 0;
setAttr "l_hand_geoShape.pnts[301].pntx" 0;
setAttr "l_hand_geoShape.pnts[302].pntx" 0;
setAttr "l_hand_geoShape.pnts[303].pntx" 0;
setAttr "l_hand_geoShape.pnts[304].pntx" 0;
setAttr "l_hand_geoShape.pnts[305].pntx" 0;
setAttr "l_hand_geoShape.pnts[306].pntx" 0;
setAttr "l_hand_geoShape.pnts[307].pntx" 0;
setAttr "l_hand_geoShape.pnts[308].pntx" 0;
setAttr "l_hand_geoShape.pnts[309].pntx" 0;
setAttr "l_hand_geoShape.pnts[310].pntx" 0;
setAttr "l_hand_geoShape.pnts[311].pntx" 0;
setAttr "l_hand_geoShape.pnts[312].pntx" 0;
setAttr "l_hand_geoShape.pnts[313].pntx" 0;
setAttr "l_hand_geoShape.pnts[314].pntx" 0;
setAttr "l_hand_geoShape.pnts[315].pntx" 0;
setAttr "l_hand_geoShape.pnts[316].pntx" 0;
setAttr "l_hand_geoShape.pnts[317].pntx" 0;
setAttr "l_hand_geoShape.pnts[318].pntx" 0;
setAttr "l_hand_geoShape.pnts[319].pntx" 0;
setAttr "l_hand_geoShape.pnts[320].pntx" 0;
setAttr "l_hand_geoShape.pnts[321].pntx" 0;
setAttr "l_hand_geoShape.pnts[322].pntx" 0;
setAttr "l_hand_geoShape.pnts[323].pntx" 0;
setAttr "l_hand_geoShape.pnts[324].pntx" 0;
setAttr "l_hand_geoShape.pnts[325].pntx" 0;
setAttr "l_hand_geoShape.pnts[326].pntx" 0;
setAttr "l_hand_geoShape.pnts[327].pntx" 0;
setAttr "l_hand_geoShape.pnts[328].pntx" 0;
setAttr "l_hand_geoShape.pnts[329].pntx" 0;
setAttr "l_hand_geoShape.pnts[330].pntx" 0;
setAttr "l_hand_geoShape.pnts[331].pntx" 0;
setAttr "l_hand_geoShape.pnts[332].pntx" 0;
setAttr "l_hand_geoShape.pnts[333].pntx" 0;
setAttr "l_hand_geoShape.pnts[334].pntx" 0;
setAttr "l_hand_geoShape.pnts[335].pntx" 0;
setAttr "l_hand_geoShape.pnts[336].pntx" 0;
setAttr "l_hand_geoShape.pnts[337].pntx" 0;
setAttr "l_hand_geoShape.pnts[338].pntx" 0;
setAttr "l_hand_geoShape.pnts[339].pntx" 0;
setAttr "l_hand_geoShape.pnts[340].pntx" 0;
setAttr "l_hand_geoShape.pnts[341].pntx" 0;
setAttr "l_hand_geoShape.pnts[342].pntx" 0;
setAttr "l_hand_geoShape.pnts[343].pntx" 0;
setAttr "l_hand_geoShape.pnts[344].pntx" 0;
setAttr "l_hand_geoShape.pnts[345].pntx" 0;
setAttr "l_hand_geoShape.pnts[346].pntx" 0;
setAttr "l_hand_geoShape.pnts[347].pntx" 0;
setAttr "l_hand_geoShape.pnts[348].pntx" 0;
setAttr "l_hand_geoShape.pnts[349].pntx" 0;
setAttr "l_hand_geoShape.pnts[350].pntx" 0;
setAttr "l_hand_geoShape.pnts[351].pntx" 0;
setAttr "l_hand_geoShape.pnts[352].pntx" 0;
setAttr "l_hand_geoShape.pnts[353].pntx" 0;
setAttr "l_hand_geoShape.pnts[354].pntx" 0;
setAttr "l_hand_geoShape.pnts[355].pntx" 0;
setAttr "l_hand_geoShape.pnts[356].pntx" 0;
setAttr "l_hand_geoShape.pnts[357].pntx" 0;
setAttr "l_hand_geoShape.pnts[358].pntx" 0;
setAttr "l_hand_geoShape.pnts[359].pntx" 0;
setAttr "l_hand_geoShape.pnts[360].pntx" 0;
setAttr "l_hand_geoShape.pnts[361].pntx" 0;
setAttr "l_hand_geoShape.pnts[362].pntx" 0;
setAttr "l_hand_geoShape.pnts[363].pntx" 0;
setAttr "l_hand_geoShape.pnts[364].pntx" 0;
setAttr "l_hand_geoShape.pnts[365].pntx" 0;
setAttr "l_hand_geoShape.pnts[366].pntx" 0;
setAttr "l_hand_geoShape.pnts[367].pntx" 0;
setAttr "l_hand_geoShape.pnts[368].pntx" 0;
setAttr "l_hand_geoShape.pnts[369].pntx" 0;
setAttr "l_hand_geoShape.pnts[370].pntx" 0;
setAttr "l_hand_geoShape.pnts[371].pntx" 0;
setAttr "l_hand_geoShape.pnts[372].pntx" 0;
setAttr "l_hand_geoShape.pnts[373].pntx" 0;
setAttr "l_hand_geoShape.pnts[374].pntx" 0;
setAttr "l_hand_geoShape.pnts[375].pntx" 0;
setAttr "l_hand_geoShape.pnts[376].pntx" 0;
setAttr "l_hand_geoShape.pnts[377].pntx" 0;
setAttr "l_hand_geoShape.pnts[378].pntx" 0;
setAttr "l_hand_geoShape.pnts[379].pntx" 0;
setAttr "l_hand_geoShape.pnts[380].pntx" 0;
setAttr "l_hand_geoShape.pnts[381].pntx" 0;
setAttr "l_hand_geoShape.pnts[382].pntx" 0;
setAttr "l_hand_geoShape.pnts[383].pntx" 0;
setAttr "l_hand_geoShape.pnts[384].pntx" 0;
setAttr "l_hand_geoShape.pnts[385].pntx" 0;
setAttr "l_hand_geoShape.pnts[386].pntx" 0;
setAttr "l_hand_geoShape.pnts[387].pntx" 0;
setAttr "l_hand_geoShape.pnts[388].pntx" 0;
setAttr "l_hand_geoShape.pnts[389].pntx" 0;
setAttr "l_hand_geoShape.pnts[390].pntx" 0;
setAttr "l_hand_geoShape.pnts[391].pntx" 0;
setAttr "l_hand_geoShape.pnts[392].pntx" 0;
setAttr "l_hand_geoShape.pnts[393].pntx" 0;
setAttr "l_hand_geoShape.pnts[394].pntx" 0;
setAttr "l_hand_geoShape.pnts[395].pntx" 0;
setAttr "l_hand_geoShape.pnts[396].pntx" 0;
setAttr "l_hand_geoShape.pnts[397].pntx" 0;
setAttr "l_hand_geoShape.pnts[398].pntx" 0;
setAttr "l_hand_geoShape.pnts[399].pntx" 0;
setAttr "l_hand_geoShape.pnts[400].pntx" 0;
setAttr "l_hand_geoShape.pnts[401].pntx" 0;
setAttr "l_hand_geoShape.pnts[402].pntx" 0;
setAttr "l_hand_geoShape.pnts[403].pntx" 0;
setAttr "l_hand_geoShape.pnts[404].pntx" 0;
setAttr "l_hand_geoShape.pnts[405].pntx" 0;
setAttr "l_hand_geoShape.pnts[406].pntx" 0;
setAttr "l_hand_geoShape.pnts[407].pntx" 0;
setAttr "l_hand_geoShape.pnts[408].pntx" 0;
setAttr "l_hand_geoShape.pnts[409].pntx" 0;
setAttr "l_hand_geoShape.pnts[410].pntx" 0;
setAttr "l_hand_geoShape.pnts[411].pntx" 0;
setAttr "l_hand_geoShape.pnts[412].pntx" 0;
setAttr "l_hand_geoShape.pnts[413].pntx" 0;
setAttr "l_hand_geoShape.pnts[414].pntx" 0;
setAttr "l_hand_geoShape.pnts[415].pntx" 0;
setAttr "l_hand_geoShape.pnts[416].pntx" 0;
setAttr "l_hand_geoShape.pnts[417].pntx" 0;
setAttr "l_hand_geoShape.pnts[418].pntx" 0;
setAttr "l_hand_geoShape.pnts[419].pntx" 0;
setAttr "l_hand_geoShape.pnts[420].pntx" 0;
setAttr "l_hand_geoShape.pnts[421].pntx" 0;
setAttr "l_hand_geoShape.pnts[422].pntx" 0;
setAttr "l_hand_geoShape.pnts[423].pntx" 0;
setAttr "l_hand_geoShape.pnts[424].pntx" 0;
setAttr "l_hand_geoShape.pnts[425].pntx" 0;
setAttr "l_hand_geoShape.pnts[426].pntx" 0;
setAttr "l_hand_geoShape.pnts[427].pntx" 0;
setAttr "l_hand_geoShape.pnts[428].pntx" 0;
setAttr "l_hand_geoShape.pnts[429].pntx" 0;
setAttr "l_hand_geoShape.pnts[430].pntx" 0;
setAttr "l_hand_geoShape.pnts[431].pntx" 0;
setAttr "l_hand_geoShape.pnts[432].pntx" 0;
setAttr "l_hand_geoShape.pnts[433].pntx" 0;
setAttr "l_hand_geoShape.pnts[434].pntx" 0;
setAttr "l_hand_geoShape.pnts[435].pntx" 0;
setAttr "l_hand_geoShape.pnts[436].pntx" 0;
setAttr "l_hand_geoShape.pnts[437].pntx" 0;
setAttr "l_hand_geoShape.pnts[438].pntx" 0;
setAttr "l_hand_geoShape.pnts[439].pntx" 0;
setAttr "l_hand_geoShape.pnts[440].pntx" 0;
setAttr "l_hand_geoShape.pnts[441].pntx" 0;
setAttr "l_hand_geoShape.pnts[442].pntx" 0;
setAttr "l_hand_geoShape.pnts[443].pntx" 0;
setAttr "l_hand_geoShape.pnts[444].pntx" 0;
setAttr "l_hand_geoShape.pnts[445].pntx" 0;
setAttr "l_hand_geoShape.pnts[446].pntx" 0;
setAttr "l_hand_geoShape.pnts[447].pntx" 0;
setAttr "l_hand_geoShape.pnts[448].pntx" 0;
setAttr "l_hand_geoShape.pnts[449].pntx" 0;
setAttr "l_hand_geoShape.pnts[450].pntx" 0;
setAttr "l_hand_geoShape.pnts[451].pntx" 0;
setAttr "l_hand_geoShape.pnts[452].pntx" 0;
setAttr "l_hand_geoShape.pnts[453].pntx" 0;
setAttr "l_hand_geoShape.pnts[454].pntx" 0;
setAttr "l_hand_geoShape.pnts[455].pntx" 0;
setAttr "l_hand_geoShape.pnts[456].pntx" 0;
setAttr "l_hand_geoShape.pnts[457].pntx" 0;
setAttr "l_hand_geoShape.pnts[458].pntx" 0;
setAttr "l_hand_geoShape.pnts[459].pntx" 0;
setAttr "l_hand_geoShape.pnts[460].pntx" 0;
setAttr "l_hand_geoShape.pnts[461].pntx" 0;
setAttr "l_hand_geoShape.pnts[462].pntx" 0;
setAttr "l_hand_geoShape.pnts[463].pntx" 0;
setAttr "l_hand_geoShape.pnts[464].pntx" 0;
setAttr "l_hand_geoShape.pnts[465].pntx" 0;
setAttr "l_hand_geoShape.pnts[466].pntx" 0;
setAttr "l_hand_geoShape.pnts[467].pntx" 0;
setAttr "l_hand_geoShape.pnts[468].pntx" 0;
setAttr "l_hand_geoShape.pnts[469].pntx" 0;
setAttr "l_hand_geoShape.pnts[470].pntx" 0;
setAttr "l_hand_geoShape.pnts[471].pntx" 0;
setAttr "l_hand_geoShape.pnts[472].pntx" 0;
setAttr "l_hand_geoShape.pnts[473].pntx" 0;
setAttr "l_hand_geoShape.pnts[474].pntx" 0;
setAttr "l_hand_geoShape.pnts[475].pntx" 0;
setAttr "l_hand_geoShape.pnts[476].pntx" 0;
setAttr "l_hand_geoShape.pnts[477].pntx" 0;
setAttr "l_hand_geoShape.pnts[478].pntx" 0;
setAttr "l_hand_geoShape.pnts[479].pntx" 0;
setAttr "l_hand_geoShape.pnts[480].pntx" 0;
setAttr "l_hand_geoShape.pnts[481].pntx" 0;
setAttr "l_hand_geoShape.pnts[482].pntx" 0;
setAttr "l_hand_geoShape.pnts[483].pntx" 0;
setAttr "l_hand_geoShape.pnts[484].pntx" 0;
setAttr "l_hand_geoShape.pnts[485].pntx" 0;
setAttr "l_hand_geoShape.pnts[486].pntx" 0;
setAttr "l_hand_geoShape.pnts[487].pntx" 0;
setAttr "l_hand_geoShape.pnts[488].pntx" 0;
setAttr "l_hand_geoShape.pnts[489].pntx" 0;
setAttr "l_hand_geoShape.pnts[490].pntx" 0;
setAttr "l_hand_geoShape.pnts[491].pntx" 0;
setAttr "l_hand_geoShape.pnts[492].pntx" 0;
setAttr "l_hand_geoShape.pnts[493].pntx" 0;
setAttr "l_hand_geoShape.pnts[494].pntx" 0;
setAttr "l_hand_geoShape.pnts[495].pntx" 0;
setAttr "l_hand_geoShape.pnts[496].pntx" 0;
setAttr "l_hand_geoShape.pnts[497].pntx" 0;
setAttr "l_hand_geoShape.pnts[498].pntx" 0;
setAttr "l_hand_geoShape.pnts[499].pntx" 0;
setAttr "l_hand_geoShape.pnts[500].pntx" 0;
setAttr "l_hand_geoShape.pnts[501].pntx" 0;
setAttr "l_hand_geoShape.pnts[502].pntx" 0;
setAttr "l_hand_geoShape.pnts[503].pntx" 0;
setAttr "l_hand_geoShape.pnts[504].pntx" 0;
setAttr "l_hand_geoShape.pnts[505].pntx" 0;
setAttr "l_hand_geoShape.pnts[506].pntx" 0;
setAttr "l_hand_geoShape.pnts[507].pntx" 0;
setAttr "l_hand_geoShape.pnts[508].pntx" 0;
setAttr "l_hand_geoShape.pnts[509].pntx" 0;
setAttr "l_hand_geoShape.pnts[510].pntx" 0;
setAttr "l_hand_geoShape.pnts[511].pntx" 0;
setAttr "l_hand_geoShape.pnts[512].pntx" 0;
setAttr "l_hand_geoShape.pnts[513].pntx" 0;
setAttr "l_hand_geoShape.pnts[514].pntx" 0;
setAttr "l_hand_geoShape.pnts[515].pntx" 0;
setAttr "l_hand_geoShape.pnts[516].pntx" 0;
setAttr "l_hand_geoShape.pnts[517].pntx" 0;
setAttr "l_hand_geoShape.pnts[518].pntx" 0;
setAttr "l_hand_geoShape.pnts[519].pntx" 0;
setAttr "l_hand_geoShape.pnts[520].pntx" 0;
setAttr "l_hand_geoShape.pnts[521].pntx" 0;
setAttr "l_hand_geoShape.pnts[522].pntx" 0;
setAttr "l_hand_geoShape.pnts[523].pntx" 0;
setAttr "l_hand_geoShape.pnts[524].pntx" 0;
setAttr "l_hand_geoShape.pnts[525].pntx" 0;
setAttr "l_hand_geoShape.pnts[526].pntx" 0;
setAttr "l_hand_geoShape.pnts[527].pntx" 0;
setAttr "l_hand_geoShape.pnts[528].pntx" 0;
setAttr "l_hand_geoShape.pnts[529].pntx" 0;
setAttr "l_hand_geoShape.pnts[530].pntx" 0;
setAttr "l_hand_geoShape.pnts[531].pntx" 0;
setAttr "l_hand_geoShape.pnts[532].pntx" 0;
setAttr "l_hand_geoShape.pnts[533].pntx" 0;
setAttr "l_hand_geoShape.pnts[534].pntx" 0;
setAttr "l_hand_geoShape.pnts[535].pntx" 0;
setAttr "l_hand_geoShape.pnts[536].pntx" 0;
setAttr "l_hand_geoShape.pnts[537].pntx" 0;
setAttr "l_hand_geoShape.pnts[538].pntx" 0;
setAttr "l_hand_geoShape.pnts[539].pntx" 0;
setAttr "l_hand_geoShape.pnts[540].pntx" 0;
setAttr "l_hand_geoShape.pnts[541].pntx" 0;
setAttr "l_hand_geoShape.pnts[542].pntx" 0;
setAttr "l_hand_geoShape.pnts[543].pntx" 0;
setAttr "l_hand_geoShape.pnts[544].pntx" 0;
setAttr "l_hand_geoShape.pnts[545].pntx" 0;
setAttr "l_hand_geoShape.pnts[546].pntx" 0;
setAttr "l_hand_geoShape.pnts[547].pntx" 0;
setAttr "l_hand_geoShape.pnts[548].pntx" 0;
setAttr "l_hand_geoShape.pnts[549].pntx" 0;
setAttr "l_hand_geoShape.pnts[550].pntx" 0;
setAttr "l_hand_geoShape.pnts[551].pntx" 0;
setAttr "l_hand_geoShape.pnts[552].pntx" 0;
setAttr "l_hand_geoShape.pnts[553].pntx" 0;
setAttr "l_hand_geoShape.pnts[554].pntx" 0;
setAttr "l_hand_geoShape.pnts[555].pntx" 0;
setAttr "l_hand_geoShape.pnts[556].pntx" 0;
setAttr "l_hand_geoShape.pnts[557].pntx" 0;
setAttr "l_hand_geoShape.pnts[558].pntx" 0;
setAttr "l_hand_geoShape.pnts[559].pntx" 0;
setAttr "l_hand_geoShape.pnts[560].pntx" 0;
setAttr "l_hand_geoShape.pnts[561].pntx" 0;
setAttr "l_hand_geoShape.pnts[562].pntx" 0;
setAttr "l_hand_geoShape.pnts[563].pntx" 0;
setAttr "l_hand_geoShape.pnts[564].pntx" 0;
setAttr "l_hand_geoShape.pnts[565].pntx" 0;
setAttr "l_hand_geoShape.pnts[566].pntx" 0;
setAttr "l_hand_geoShape.pnts[567].pntx" 0;
setAttr "l_hand_geoShape.pnts[568].pntx" 0;
setAttr "l_hand_geoShape.pnts[569].pntx" 0;
setAttr "l_hand_geoShape.pnts[570].pntx" 0;
setAttr "l_hand_geoShape.pnts[571].pntx" 0;
setAttr "l_hand_geoShape.pnts[572].pntx" 0;
setAttr "l_hand_geoShape.pnts[573].pntx" 0;
setAttr "l_hand_geoShape.pnts[574].pntx" 0;
setAttr "l_hand_geoShape.pnts[575].pntx" 0;
setAttr "l_hand_geoShape.pnts[576].pntx" 0;
setAttr "l_hand_geoShape.pnts[577].pntx" 0;
setAttr "l_hand_geoShape.pnts[578].pntx" 0;
setAttr "l_hand_geoShape.pnts[579].pntx" 0;
setAttr "l_hand_geoShape.pnts[580].pntx" 0;
setAttr "l_hand_geoShape.pnts[581].pntx" 0;
setAttr "l_hand_geoShape.pnts[582].pntx" 0;
setAttr "l_hand_geoShape.pnts[583].pntx" 0;
setAttr "l_hand_geoShape.pnts[584].pntx" 0;
setAttr "l_hand_geoShape.pnts[585].pntx" 0;
setAttr "l_hand_geoShape.pnts[586].pntx" 0;
setAttr "l_hand_geoShape.pnts[587].pntx" 0;
setAttr "l_hand_geoShape.pnts[588].pntx" 0;
setAttr "l_hand_geoShape.pnts[589].pntx" 0;
setAttr "l_hand_geoShape.pnts[590].pntx" 0;
setAttr "l_hand_geoShape.pnts[591].pntx" 0;
setAttr "l_hand_geoShape.pnts[592].pntx" 0;
setAttr "l_hand_geoShape.pnts[593].pntx" 0;
setAttr "l_hand_geoShape.pnts[594].pntx" 0;
setAttr "l_hand_geoShape.pnts[595].pntx" 0;
setAttr "l_hand_geoShape.pnts[596].pntx" 0;
setAttr "l_hand_geoShape.pnts[597].pntx" 0;
setAttr "l_hand_geoShape.pnts[598].pntx" 0;
setAttr "l_hand_geoShape.pnts[599].pntx" 0;
setAttr "l_hand_geoShape.pnts[600].pntx" 0;
setAttr "l_hand_geoShape.pnts[601].pntx" 0;
setAttr "l_hand_geoShape.pnts[602].pntx" 0;
setAttr "l_hand_geoShape.pnts[603].pntx" 0;
setAttr "l_hand_geoShape.pnts[604].pntx" 0;
setAttr "l_hand_geoShape.pnts[605].pntx" 0;
setAttr "l_hand_geoShape.pnts[606].pntx" 0;
setAttr "l_hand_geoShape.pnts[607].pntx" 0;
setAttr "l_hand_geoShape.pnts[608].pntx" 0;
setAttr "l_hand_geoShape.pnts[609].pntx" 0;
setAttr "l_hand_geoShape.pnts[610].pntx" 0;
setAttr "l_hand_geoShape.pnts[611].pntx" 0;
setAttr "l_hand_geoShape.pnts[612].pntx" 0;
setAttr "l_hand_geoShape.pnts[613].pntx" 0;
setAttr "l_hand_geoShape.pnts[614].pntx" 0;
setAttr "l_hand_geoShape.pnts[615].pntx" 0;
setAttr "l_hand_geoShape.pnts[616].pntx" 0;
setAttr "l_hand_geoShape.pnts[617].pntx" 0;
setAttr "l_hand_geoShape.pnts[618].pntx" 0;
setAttr "l_hand_geoShape.pnts[619].pntx" 0;
setAttr "l_hand_geoShape.pnts[620].pntx" 0;
setAttr "l_hand_geoShape.pnts[621].pntx" 0;
setAttr "l_hand_geoShape.pnts[622].pntx" 0;
setAttr "l_hand_geoShape.pnts[623].pntx" 0;
setAttr "l_hand_geoShape.pnts[624].pntx" 0;
setAttr "l_hand_geoShape.pnts[625].pntx" 0;
setAttr "l_hand_geoShape.pnts[626].pntx" 0;
setAttr "l_hand_geoShape.pnts[627].pntx" 0;
setAttr "l_hand_geoShape.pnts[628].pntx" 0;
setAttr "l_hand_geoShape.pnts[629].pntx" 0;
setAttr "l_hand_geoShape.pnts[630].pntx" 0;
setAttr "l_hand_geoShape.pnts[631].pntx" 0;
setAttr "l_hand_geoShape.pnts[632].pntx" 0;
setAttr "l_hand_geoShape.pnts[633].pntx" 0;
setAttr "l_hand_geoShape.pnts[634].pntx" 0;
setAttr "l_hand_geoShape.pnts[635].pntx" 0;
setAttr "l_hand_geoShape.pnts[636].pntx" 0;
setAttr "l_hand_geoShape.pnts[637].pntx" 0;
setAttr "l_hand_geoShape.pnts[638].pntx" 0;
setAttr "l_hand_geoShape.pnts[639].pntx" 0;
setAttr "l_hand_geoShape.pnts[640].pntx" 0;
setAttr "l_hand_geoShape.pnts[641].pntx" 0;
setAttr "l_hand_geoShape.pnts[642].pntx" 0;
setAttr "l_hand_geoShape.pnts[643].pntx" 0;
setAttr "l_hand_geoShape.pnts[644].pntx" 0;
setAttr "l_hand_geoShape.pnts[645].pntx" 0;
setAttr "l_hand_geoShape.pnts[646].pntx" 0;
setAttr "l_hand_geoShape.pnts[647].pntx" 0;
setAttr "l_hand_geoShape.pnts[648].pntx" 0;
setAttr "l_hand_geoShape.pnts[649].pntx" 0;
setAttr "l_hand_geoShape.pnts[650].pntx" 0;
setAttr "l_hand_geoShape.pnts[651].pntx" 0;
setAttr "l_hand_geoShape.pnts[652].pntx" 0;
setAttr "l_hand_geoShape.pnts[653].pntx" 0;
setAttr "l_hand_geoShape.pnts[654].pntx" 0;
setAttr "l_hand_geoShape.pnts[655].pntx" 0;
setAttr "l_hand_geoShape.pnts[656].pntx" 0;
setAttr "l_hand_geoShape.pnts[657].pntx" 0;
setAttr "l_hand_geoShape.pnts[658].pntx" 0;
setAttr "l_hand_geoShape.pnts[659].pntx" 0;
setAttr "l_hand_geoShape.pnts[660].pntx" 0;
setAttr "l_hand_geoShape.pnts[661].pntx" 0;
setAttr "l_hand_geoShape.pnts[662].pntx" 0;
setAttr "l_hand_geoShape.pnts[663].pntx" 0;
setAttr "l_hand_geoShape.pnts[664].pntx" 0;
setAttr "l_hand_geoShape.pnts[665].pntx" 0;
setAttr "l_hand_geoShape.pnts[666].pntx" 0;
setAttr "l_hand_geoShape.pnts[667].pntx" 0;
setAttr "l_hand_geoShape.pnts[668].pntx" 0;
setAttr "l_hand_geoShape.pnts[669].pntx" 0;
setAttr "l_hand_geoShape.pnts[670].pntx" 0;
setAttr "l_hand_geoShape.pnts[671].pntx" 0;
setAttr "l_hand_geoShape.pnts[672].pntx" 0;
setAttr "l_hand_geoShape.pnts[673].pntx" 0;
setAttr "l_hand_geoShape.pnts[674].pntx" 0;
setAttr "l_hand_geoShape.pnts[675].pntx" 0;
setAttr "l_hand_geoShape.pnts[676].pntx" 0;
setAttr "l_hand_geoShape.pnts[677].pntx" 0;
setAttr "l_hand_geoShape.pnts[678].pntx" 0;
setAttr "l_hand_geoShape.pnts[679].pntx" 0;
setAttr "l_hand_geoShape.pnts[680].pntx" 0;
setAttr "l_hand_geoShape.pnts[681].pntx" 0;
setAttr "l_hand_geoShape.pnts[682].pntx" 0;
setAttr "l_hand_geoShape.pnts[683].pntx" 0;
setAttr "l_hand_geoShape.pnts[684].pntx" 0;
setAttr "l_hand_geoShape.pnts[685].pntx" 0;
setAttr "l_hand_geoShape.pnts[686].pntx" 0;
setAttr "l_hand_geoShape.pnts[687].pntx" 0;
setAttr "l_hand_geoShape.pnts[688].pntx" 0;
setAttr "l_hand_geoShape.pnts[689].pntx" 0;
setAttr "l_hand_geoShape.pnts[690].pntx" 0;
setAttr "l_hand_geoShape.pnts[691].pntx" 0;
setAttr "l_hand_geoShape.pnts[692].pntx" 0;
setAttr "l_hand_geoShape.pnts[693].pntx" 0;
setAttr "l_hand_geoShape.pnts[694].pntx" 0;
setAttr "l_hand_geoShape.pnts[695].pntx" 0;
setAttr "l_hand_geoShape.pnts[696].pntx" 0;
setAttr "l_hand_geoShape.pnts[697].pntx" 0;
setAttr "l_hand_geoShape.pnts[698].pntx" 0;
setAttr "l_hand_geoShape.pnts[699].pntx" 0;
setAttr "l_hand_geoShape.pnts[700].pntx" 0;
setAttr "l_hand_geoShape.pnts[701].pntx" 0;
setAttr "l_hand_geoShape.pnts[702].pntx" 0;
setAttr "l_hand_geoShape.pnts[703].pntx" 0;
setAttr "l_hand_geoShape.pnts[704].pntx" 0;
setAttr "l_hand_geoShape.pnts[705].pntx" 0;
setAttr "l_hand_geoShape.pnts[706].pntx" 0;
setAttr "l_hand_geoShape.pnts[707].pntx" 0;
setAttr "l_hand_geoShape.pnts[708].pntx" 0;
setAttr "l_hand_geoShape.pnts[709].pntx" 0;
setAttr "l_hand_geoShape.pnts[710].pntx" 0;
setAttr "l_hand_geoShape.pnts[711].pntx" 0;
setAttr "l_hand_geoShape.pnts[712].pntx" 0;
setAttr "l_hand_geoShape.pnts[713].pntx" 0;
setAttr "l_hand_geoShape.pnts[714].pntx" 0;
setAttr "l_hand_geoShape.pnts[715].pntx" 0;
setAttr "l_hand_geoShape.pnts[716].pntx" 0;
setAttr "l_hand_geoShape.pnts[717].pntx" 0;
setAttr "l_hand_geoShape.pnts[718].pntx" 0;
setAttr "l_hand_geoShape.pnts[719].pntx" 0;
setAttr "l_hand_geoShape.pnts[720].pntx" 0;
setAttr "l_hand_geoShape.pnts[721].pntx" 0;
setAttr "l_hand_geoShape.pnts[722].pntx" 0;
setAttr "l_hand_geoShape.pnts[723].pntx" 0;
setAttr "l_hand_geoShape.pnts[724].pntx" 0;
setAttr "l_hand_geoShape.pnts[725].pntx" 0;
setAttr "l_hand_geoShape.pnts[726].pntx" 0;
setAttr "l_hand_geoShape.pnts[727].pntx" 0;
setAttr "l_hand_geoShape.pnts[728].pntx" 0;
setAttr "l_hand_geoShape.pnts[729].pntx" 0;
setAttr "l_hand_geoShape.pnts[730].pntx" 0;
setAttr "l_hand_geoShape.pnts[731].pntx" 0;
setAttr "l_hand_geoShape.pnts[732].pntx" 0;
setAttr "l_hand_geoShape.pnts[733].pntx" 0;
setAttr "l_hand_geoShape.pnts[734].pntx" 0;
setAttr "l_hand_geoShape.pnts[735].pntx" 0;
setAttr "l_hand_geoShape.pnts[736].pntx" 0;
setAttr "l_hand_geoShape.pnts[737].pntx" 0;
setAttr "l_hand_geoShape.pnts[738].pntx" 0;
setAttr "l_hand_geoShape.pnts[739].pntx" 0;
setAttr "l_hand_geoShape.pnts[740].pntx" 0;
setAttr "l_hand_geoShape.pnts[741].pntx" 0;
setAttr "l_hand_geoShape.pnts[742].pntx" 0;
setAttr "l_hand_geoShape.pnts[743].pntx" 0;
setAttr "l_hand_geoShape.pnts[744].pntx" 0;
setAttr "l_hand_geoShape.pnts[745].pntx" 0;
setAttr "l_hand_geoShape.pnts[746].pntx" 0;
setAttr "l_hand_geoShape.pnts[747].pntx" 0;
setAttr "l_hand_geoShape.pnts[748].pntx" 0;
setAttr "l_hand_geoShape.pnts[749].pntx" 0;
setAttr "l_hand_geoShape.pnts[750].pntx" 0;
setAttr "l_hand_geoShape.pnts[751].pntx" 0;
setAttr "l_hand_geoShape.pnts[752].pntx" 0;
setAttr "l_hand_geoShape.pnts[753].pntx" 0;
setAttr "l_hand_geoShape.pnts[754].pntx" 0;
setAttr "l_hand_geoShape.pnts[755].pntx" 0;
setAttr "l_hand_geoShape.pnts[756].pntx" 0;
setAttr "l_hand_geoShape.pnts[757].pntx" 0;
setAttr "l_hand_geoShape.pnts[758].pntx" 0;
setAttr "l_hand_geoShape.pnts[759].pntx" 0;
setAttr "l_hand_geoShape.pnts[760].pntx" 0;
setAttr "l_hand_geoShape.pnts[761].pntx" 0;
setAttr "l_hand_geoShape.pnts[762].pntx" 0;
setAttr "l_hand_geoShape.pnts[763].pntx" 0;
setAttr "l_hand_geoShape.pnts[764].pntx" 0;
setAttr "l_hand_geoShape.pnts[765].pntx" 0;
setAttr "l_hand_geoShape.pnts[766].pntx" 0;
// Undo: select -r l_hand_geo.vtx[0:766] 
isolateSelect -state 0 modelPanel4;
select -cl  ;
select -r l_hand_geo ;
select -cl  ;
select -r spineA_jnt ;
selectKey -clear ;
// 0 // 
select -cl  ;
select -r spineB_jnt ;
selectKey -clear ;
// 0 // 
select -r spineA_jnt ;
selectKey -clear ;
// 0 // 
select -r chest_jnt ;
selectKey -clear ;
// 0 // 
select -r neck_jnt ;
selectKey -clear ;
// 0 // 
select -r chest_jnt ;
selectKey -clear ;
// 0 // 
select -r spineB_jnt ;
selectKey -clear ;
// 0 // 
select -r spineB_jnt ;
selectKey -clear ;
// 0 // 
select -r spineA_jnt ;
selectKey -clear ;
// 0 // 
select -r root_jnt ;
selectKey -clear ;
// 0 // 
select -r head_jnt ;
selectKey -clear ;
// 0 // 
select -r r_wrist ;
selectKey -clear ;
// 0 // 
pickWalk -d up;
// r_loarm // 
pickWalk -d up;
// r_uparm // 
pickWalk -d up;
// r_clavicle // 
pickWalk -d down;
// r_uparm // 
pickWalk -d up;
// r_clavicle // 
select -r r_clavicle ;
selectKey -clear ;
// 0 // 
pickWalk -d up;
// chest_jnt // 
select -r chest_jnt ;
selectKey -clear ;
// 0 // 
pickWalk -d down;
// neck_jnt // 
pickWalk -d down;
// head_jnt // 
pickWalk -d down;
// head_jnt // 
pickWalk -d down;
// head_jnt // 
pickWalk -d down;
// head_jnt // 
select -r r_wrist ;
selectKey -clear ;
// 0 // 
pickWalk -d up;
// r_loarm // 
pickWalk -d up;
// r_uparm // 
pickWalk -d up;
// r_clavicle // 
pickWalk -d up;
// chest_jnt // 
pickWalk -d up;
// spineB_jnt // 
pickWalk -d up;
// spineA_jnt // 
pickWalk -d up;
// root_jnt // 
pickWalk -d up;
// root_jnt // 
pickWalk -d up;
// root_jnt // 
select -r l_wrist ;
selectKey -clear ;
// 0 // 
pickWalk -d up;
// l_loarm // 
pickWalk -d up;
// l_uparm // 
pickWalk -d up;
// l_clavicle // 
pickWalk -d up;
// chest_jnt // 
pickWalk -d up;
// spineB_jnt // 
pickWalk -d up;
// spineA_jnt // 
pickWalk -d up;
// root_jnt // 
select -r l_clavicle ;
selectKey -clear ;
// 0 // 
select -r head_jnt ;
selectKey -clear ;
// 0 // 
pickWalk -d up;
// neck_jnt // 
pickWalk -d up;
// chest_jnt // 
pickWalk -d up;
// spineB_jnt // 
pickWalk -d up;
// spineA_jnt // 
pickWalk -d up;
// root_jnt // 
pickWalk -d up;
// root_jnt // 
select -r l_toe ;
selectKey -clear ;
// 0 // 
pickWalk -d up;
// l_ball // 
pickWalk -d up;
// l_foot // 
pickWalk -d up;
// l_loleg // 
pickWalk -d up;
// l_upleg // 
pickWalk -d up;
// root_jnt // 
pickWalk -d up;
// root_jnt // 
select -r r_ball ;
selectKey -clear ;
// 0 // 
select -r r_toe ;
selectKey -clear ;
// 0 // 
pickWalk -d up;
// r_ball // 
pickWalk -d up;
// r_foot // 
pickWalk -d up;
// r_loleg // 
pickWalk -d up;
// r_upleg // 
pickWalk -d up;
// root_jnt // 
pickWalk -d up;
// root_jnt // 
select -r r_toe ;
selectKey -clear ;
// 0 // 
pickWalk -d up;
// r_ball // 
pickWalk -d up;
// r_foot // 
pickWalk -d up;
// r_loleg // 
pickWalk -d up;
// r_upleg // 
pickWalk -d up;
// root_jnt // 
select -r root_jnt ;
selectKey -clear ;
// 0 // 
select -r spineA_jnt ;
selectKey -clear ;
// 0 // 
select -r spineA_jnt ;
selectKey -clear ;
// 0 // 
select -r spineB_jnt ;
selectKey -clear ;
// 0 // 
select -r chest_jnt ;
selectKey -clear ;
// 0 // 
select -r neck_jnt ;
selectKey -clear ;
// 0 // 
select -r head_jnt ;
selectKey -clear ;
// 0 // 
select -r l_clavicle ;
selectKey -clear ;
// 0 // 
select -r l_uparm ;
selectKey -clear ;
// 0 // 
select -r l_loarm ;
selectKey -clear ;
// 0 // 
pickWalk -d down;
// l_wrist // 
pickWalk -d down;
// l_wrist // 
select -r r_uparm ;
selectKey -clear ;
// 0 // 
select -r r_clavicle ;
selectKey -clear ;
// 0 // 
pickWalk -d down;
// r_uparm // 
pickWalk -d down;
// r_loarm // 
pickWalk -d down;
// r_wrist // 
pickWalk -d down;
// r_wrist // 
select -r l_upleg ;
selectKey -clear ;
// 0 // 
pickWalk -d down;
// l_loleg // 
pickWalk -d down;
// l_foot // 
pickWalk -d down;
// l_ball // 
pickWalk -d down;
// l_toe // 
select -r r_upleg ;
selectKey -clear ;
// 0 // 
pickWalk -d down;
// r_loleg // 
pickWalk -d down;
// r_foot // 
pickWalk -d down;
// r_ball // 
pickWalk -d up;
// r_foot // 
pickWalk -d up;
// r_loleg // 
pickWalk -d up;
// r_upleg // 
pickWalk -d down;
// r_loleg // 
pickWalk -d down;
// r_foot // 
pickWalk -d down;
// r_ball // 
pickWalk -d down;
// r_toe // 
pickWalk -d down;
// r_toe // 
select -r l_loleg ;
selectKey -clear ;
// 0 // 
select -r l_loleg ;
selectKey -clear ;
// 0 // 
select -r l_foot ;
selectKey -clear ;
// 0 // 
select -r l_loleg ;
selectKey -clear ;
// 0 // 
pickWalk -d up;
// l_upleg // 
joint -e  -oj xzy -secondaryAxisOrient xdown -zso;
pickWalk -d down;
// l_loleg // 
pickWalk -d down;
// l_foot // 
pickWalk -d down;
// l_ball // 
pickWalk -d down;
// l_toe // 
pickWalk -d down;
// l_toe // 
pickWalk -d down;
// l_toe // 
select -r r_upleg ;
selectKey -clear ;
// 0 // 
pickWalk -d down;
// r_loleg // 
pickWalk -d up;
// r_upleg // 
joint -e  -oj xzy -secondaryAxisOrient xdown -zso;
// Undo: if (`window -exists OptionBoxWindow`) deleteUI -window OptionBoxWindow
// Undo: jointOrientCallback OptionBoxWindow|formLayout93|tabLayout4|formLayout95|tabLayout5|columnLayout44 1; hideOptionBox
pickWalk -d down;
// r_loleg // 
pickWalk -d down;
// r_foot // 
pickWalk -d up;
// r_loleg // 
pickWalk -d down;
// r_foot // 
pickWalk -d down;
// r_ball // 
pickWalk -d up;
// r_foot // 
pickWalk -d up;
// r_loleg // 
pickWalk -d up;
// r_upleg // 
select -r r_upleg ;
selectKey -clear ;
// 0 // 
select -r r_upleg r_loleg r_foot r_ball r_toe ;
selectKey -clear ;
// 0 // 
select -r root_jnt ;
selectKey -clear ;
// 0 // 
select -r r_upleg ;
selectKey -clear ;
// 0 // 
select -r r_upleg r_loleg r_foot r_ball r_toe ;
selectKey -clear ;
// 0 // 
select -r l_upleg ;
selectKey -clear ;
// 0 // 
select -r l_upleg l_loleg l_foot l_ball l_toe ;
selectKey -clear ;
// 0 // 
mirrorJoint -mirrorYZ -mirrorBehavior -searchReplace "l_" "r_";
// Error: line 0: Too many arguments.  Expected 1, found 0. // 
select -r l_upleg ;
selectKey -clear ;
// 0 // 
mirrorJoint -mirrorYZ -mirrorBehavior -searchReplace "l_" "r_";
// r_upleg r_loleg r_foot r_ball r_toe // 
pickWalk -d down;
// r_loleg // 
pickWalk -d down;
// r_foot // 
select -r r_upleg ;
selectKey -clear ;
// 0 // 
pickWalk -d up;
// root_jnt // 
pickWalk -d up;
// root_jnt // 
pickWalk -d up;
// root_jnt // 
pickWalk -d up;
// root_jnt // 
pickWalk -d down;
// spineA_jnt // 
pickWalk -d up;
// root_jnt // 
pickWalk -d down;
// spineA_jnt // 
pickWalk -d down;
// spineB_jnt // 
pickWalk -d down;
// chest_jnt // 
pickWalk -d up;
// spineB_jnt // 
pickWalk -d up;
// spineA_jnt // 
select -r r_wrist ;
selectKey -clear ;
// 0 // 
pickWalk -d up;
// r_loarm // 
pickWalk -d down;
// r_wrist // 
pickWalk -d up;
// r_loarm // 
pickWalk -d up;
// r_uparm // 
pickWalk -d up;
// r_clavicle // 
select -r r_loarm ;
selectKey -clear ;
// 0 // 
pickWalk -d down;
// r_wrist // 
pickWalk -d up;
// r_loarm // 
pickWalk -d down;
// r_wrist // 
pickWalk -d up;
// r_loarm // 
pickWalk -d up;
// r_uparm // 
select -r l_wrist ;
selectKey -clear ;
// 0 // 
select -r l_upleg ;
selectKey -clear ;
// 0 // 
select -cl  ;
select -r l_loleg ;
selectKey -clear ;
// 0 // 
select -r l_foot ;
selectKey -clear ;
// 0 // 
pickWalk -d down;
// l_ball // 
pickWalk -d up;
// l_foot // 
pickWalk -d up;
// l_loleg // 
pickWalk -d up;
// l_upleg // 
pickWalk -d down;
// l_loleg // 
pickWalk -d up;
// l_upleg // 
pickWalk -d up;
// root_jnt // 
pickWalk -d down;
// spineA_jnt // 
pickWalk -d down;
// spineB_jnt // 
pickWalk -d down;
// chest_jnt // 
pickWalk -d down;
// neck_jnt // 
pickWalk -d down;
// head_jnt // 
pickWalk -d down;
// head_jnt // 
pickWalk -d up;
// neck_jnt // 
pickWalk -d up;
// chest_jnt // 
pickWalk -d up;
// spineB_jnt // 
pickWalk -d up;
// spineA_jnt // 
pickWalk -d up;
// root_jnt // 
pickWalk -d down;
// spineA_jnt // 
pickWalk -d down;
// spineB_jnt // 
pickWalk -d down;
// chest_jnt // 
pickWalk -d down;
// neck_jnt // 
pickWalk -d down;
// head_jnt // 
pickWalk -d down;
// head_jnt // 
pickWalk -d down;
// head_jnt // 
pickWalk -d up;
// neck_jnt // 
pickWalk -d up;
// chest_jnt // 
pickWalk -d up;
// spineB_jnt // 
pickWalk -d up;
// spineA_jnt // 
pickWalk -d up;
// root_jnt // 
pickWalk -d up;
// root_jnt // 
pickWalk -d up;
// root_jnt // 
select -r l_wrist ;
selectKey -clear ;
// 0 // 
select -r l_toe ;
selectKey -clear ;
// 0 // 
pickWalk -d up;
// l_ball // 
pickWalk -d up;
// l_foot // 
pickWalk -d down;
// l_ball // 
pickWalk -d down;
// l_toe // 
pickWalk -d up;
// l_ball // 
pickWalk -d up;
// l_foot // 
pickWalk -d down;
// l_ball // 
pickWalk -d down;
// l_toe // 
pickWalk -d up;
// l_ball // 
pickWalk -d up;
// l_foot // 
pickWalk -d up;
// l_loleg // 
pickWalk -d up;
// l_upleg // 
pickWalk -d down;
// l_loleg // 
pickWalk -d down;
// l_foot // 
pickWalk -d down;
// l_ball // 
pickWalk -d down;
// l_toe // 
pickWalk -d down;
// l_toe // 
select -cl  ;
select -r l_uparm ;
rotate -r -os -fo 0 1.137938 0 ;
makeIdentity -apply true -t 0 -r 1 -s 0 -n 0 -pn 1;
pickWalk -d down;
// l_loarm // 
pickWalk -d up;
// l_uparm // 
pickWalk -d down;
// l_loarm // 
pickWalk -d up;
// l_uparm // 
pickWalk -d up;
// l_clavicle // 
pickWalk -d down;
// l_uparm // 
pickWalk -d down;
// l_loarm // 
pickWalk -d down;
// l_wrist // 
pickWalk -d down;
// l_wrist // 
pickWalk -d up;
// l_loarm // 
pickWalk -d up;
// l_uparm // 
pickWalk -d up;
// l_clavicle // 
pickWalk -d up;
// chest_jnt // 
pickWalk -d down;
// neck_jnt // 
pickWalk -d down;
// head_jnt // 
pickWalk -d down;
// head_jnt // 
pickWalk -d down;
// head_jnt // 
pickWalk -d down;
// head_jnt // 
pickWalk -d up;
// neck_jnt // 
pickWalk -d up;
// chest_jnt // 
setAttr "chest_jnt.jointOrientY" -0.4904;
setAttr "chest_jnt.jointOrientY" 0;
// Undo: setAttr
setAttr "chest_jnt.jointOrientY" 0;
// Undo: setAttr
// Undo: setAttr
// Undo: PickWalkUp
// Undo: PickWalkUp
// Undo: PickWalkDown
// Undo: PickWalkDown
// Undo: PickWalkDown
// Undo: PickWalkDown
// Undo: PickWalkDown
// Undo: PickWalkUp
// Undo: PickWalkUp
// Undo: PickWalkUp
// Undo: PickWalkUp
// Undo: PickWalkDown
// Undo: PickWalkDown
// Undo: PickWalkDown
// Undo: PickWalkDown
// Undo: PickWalkUp
// Undo: PickWalkUp
// Undo: PickWalkDown
// Undo: PickWalkUp
// Undo: PickWalkDown
// Undo: if (`window -exists OptionBoxWindow`) deleteUI -window OptionBoxWindow
// Undo: performFreezeTransformationsCallback OptionBoxWindow|formLayout104|tabLayout8|formLayout106|tabLayout9|columnLayout60 1; hideOptionBox
// Undo: rotate -r -os -fo 0 1.137938 0 
select -r r_clavicle ;
selectKey -clear ;
// 0 // 
select -r chest_jnt ;
selectKey -clear ;
// 0 // 
displaySmoothness -polygonObject 0;
setAttr "chest_jnt.jointOrientY" 0;
select -r l_clavicle ;
selectKey -clear ;
// 0 // 
select -r r_clavicle ;
selectKey -clear ;
// 0 // 
select -r r_clavicle r_uparm r_loarm r_wrist ;
selectKey -clear ;
// 0 // 
select -r l_clavicle ;
selectKey -clear ;
// 0 // 
mirrorJoint -mirrorYZ -mirrorBehavior -searchReplace "l_" "r_";
// r_clavicle r_uparm r_loarm r_wrist // 
select -r root_jnt ;
selectKey -clear ;
// 0 // 
select -cl  ;
select -r l_hand_geo ;
select -cl  ;
select -r l_wrist ;
selectKey -clear ;
// 0 // 
move -r -ls -wd -0.276272 0 0 ;
select -r l_upleg ;
selectKey -clear ;
// 0 // 
select -r r_clavicle ;
selectKey -clear ;
// 0 // 
select -r l_clavicle ;
selectKey -clear ;
// 0 // 
joint -e  -oj xzy -secondaryAxisOrient xdown -zso;
// Undo: OrientJoint
mirrorJoint -mirrorYZ -mirrorBehavior -searchReplace "l_" "r_";
// r_clavicle r_uparm r_loarm r_wrist // 
select -r l_clavicle ;
selectKey -clear ;
// 0 // 
select -cl  ;
select -r root_geo ;
selectKey -clear ;
// 0 // 
select -cl  ;
select -r chest_geo ;
select -cl  ;
select -r l_hand_geo ;
select -cl  ;
select -r l_wrist ;
select -tgl l_hand_geo ;
select -r l_hand_geo ;
setAttr -k on |root_geo|spine_A_geo|spine_B_geo|chest_geo|l_clavicle_geo|l_upArm_geo|l_loArm_geo|l_hand_geo.translateX;
setAttr -k on |root_geo|spine_A_geo|spine_B_geo|chest_geo|l_clavicle_geo|l_upArm_geo|l_loArm_geo|l_hand_geo.translateY;
setAttr -k on |root_geo|spine_A_geo|spine_B_geo|chest_geo|l_clavicle_geo|l_upArm_geo|l_loArm_geo|l_hand_geo.translateZ;
// Undo: PS_moveToKeyable Keyable l_hand_geo
select -r l_loarm ;
selectKey -clear ;
// 0 // 
select -r l_wrist ;
selectKey -clear ;
// 0 // 
select -cl  ;
select -r l_wrist ;
rotate -r -os -fo 0 0 -72.689898 ;
select -cl  ;
// Undo: select -cl  
// Undo: rotate -r -os -fo 0 0 -72.689898 
select -cl  ;
select -r l_hand_geo ;
select -r l_wrist ;
selectKey -clear ;
// 0 // 
rotate -r -os -fo 0 0 -128.654794 ;
select -cl  ;
// Undo: select -cl  
// Undo: rotate -r -os -fo 0 0 -128.654794 
// Undo: select -r l_wrist 
pickWalk -d up;
// l_loArm_geo // 
pickWalk -d down;
// l_loArm_geoShape // 
pickWalk -d down;
// l_loArm_geoShape // 
pickWalk -d down;
// l_loArm_geoShape // 
pickWalk -d down;
// l_loArm_geoShape // 
pickWalk -d up;
// l_loArm_geo // 
pickWalk -d up;
// l_upArm_geo // 
pickWalk -d down;
// l_upArm_geoShape // 
pickWalk -d down;
// l_upArm_geoShape // 
pickWalk -d down;
// l_upArm_geoShape // 
pickWalk -d up;
// l_upArm_geo // 
pickWalk -d down;
// l_upArm_geoShape // 
pickWalk -d up;
// l_upArm_geo // 
pickWalk -d up;
// l_clavicle_geo // 
pickWalk -d up;
// chest_geo // 
pickWalk -d down;
// chest_geoShape // 
pickWalk -d down;
// chest_geoShape // 
pickWalk -d down;
// chest_geoShape // 
pickWalk -d down;
// chest_geoShape // 
select -r l_clavicle ;
selectKey -clear ;
// 0 // 
select -r l_wrist ;
selectKey -clear ;
// 0 // 
select -r l_wrist ;
selectKey -clear ;
// 0 // 
rotate -r -os -fo 97.095707 -0.156948 -247.706187 ;
// Undo: rotate -r -os -fo 97.095707 -0.156948 -247.706187 
select -cl  ;
select -r l_hand_geo ;
select -cl  ;
select -r l_wrist ;
setAttr "l_wrist.rotateZ" 30;
// Undo: setAttr
// Undo: select -r l_wrist 
// Undo: select -cl  
// Undo: select -r l_hand_geo 
// Undo: select -cl  
// Undo: select -r l_wrist 
// Undo: select -r l_wrist 
// Undo: select -r l_clavicle 
// Undo: PickWalkDown
// Undo: PickWalkDown
// Undo: PickWalkDown
// Undo: PickWalkDown
// Undo: PickWalkUp
// Undo: PickWalkUp
// Undo: PickWalkUp
// Undo: PickWalkDown
// Undo: PickWalkUp
// Undo: PickWalkDown
// Undo: PickWalkDown
// Undo: PickWalkDown
// Undo: PickWalkUp
// Undo: PickWalkUp
// Undo: PickWalkDown
// Undo: PickWalkDown
// Undo: PickWalkDown
// Undo: PickWalkDown
// Undo: PickWalkUp
// Undo: select -r l_hand_geo 
// Undo: select -cl  
// Undo: select -r l_wrist 
// Undo: select -cl  
// Undo: select -r l_wrist 
// Undo: select -r l_loarm 
// Undo: select -r l_hand_geo 
// Undo: if (`window -exists OptionBoxWindow`) deleteUI -window OptionBoxWindow
// Undo: skinClusterCallback OptionBoxWindow|formLayout112|tabLayout12|formLayout114|tabLayout13|columnLayout62 1; hideOptionBox
// Undo: select -tgl l_hand_geo 
select -cl  ;
select -r l_loArm_geo ;
select -r l_wrist ;
select -tgl l_hand_geo ;
rotate -r -os -fo 0 0 1.865835 ;
// Undo: rotate -r -os -fo 0 0 1.865835 
select -r l_hand_geo ;
select -addFirst skinCluster1 ;
select -r l_hand_geo ;
select -r l_hand_geo ;
select -addFirst skinCluster1 ;
rename "skinCluster1" "l_hand_geo_sCls";
// l_hand_geo_sCls // 
select -d l_hand_geo_sCls ;
select -addFirst tweak1 ;
select -cl  ;
select -r l_hand_geo ;
select -cl  ;
select -cl  ;
select -cl  ;
select -r l_hand_geoShapeOrig ;
select -r l_hand_geoShapeOrig ;
select -r tweak1 ;
select -r -ne tweakSet1 ;
select -r -ne tweakSet1 ;
select -r l_hand_geo_sCls ;
select -r l_hand_geo_sCls ;
select -cl  ;
select -r l_hand_geoShape ;
select -r l_hand_geoShapeOrig ;
select -r tweak1 ;
select -r tweak1 ;
select -r l_hand_geoShape ;
select -r tweak1 l_hand_geoShapeOrig ;
select -cl  ;
select -r tweak1 l_hand_geoShapeOrig ;
select -cl  ;
select -r tweak1 l_hand_geoShapeOrig ;
select -cl  ;
select -r l_loArm_geo ;
select -cl  ;
select -r l_loarm ;
rotate -r -os -fo 0.229912 -0.0609378 -0.00649548 ;
// Undo: rotate -r -os -fo 0.229912 -0.0609378 -0.00649548 
select -tgl l_loArm_geo ;
// Error: line 0: Selected geometry `l_hand_geo` is already connected to a skinCluster // 
select -r l_loArm_geo ;
select -cl  ;
// Undo: select -cl  
// Undo: select -r l_loArm_geo 
// Undo: SmoothBindSkin
// Undo: select -tgl l_loArm_geo 
select -r root_geo ;
selectKey -clear ;
// 0 // 
select -r root_geo spine_A_geo spine_B_geo chest_geo l_clavicle_geo l_upArm_geo l_loArm_geo l_hand_geo r_clavicle_geo r_upArm_geo r_loArm_geo r_hand_geo neck_geo head_geo l_upLeg_geo l_loLeg_geo l_foot_geo l_toe_geo r_upLeg_geo r_loLeg_geo r_foot_geo r_toe_geo ;
selectKey -clear ;
// 0 // 
select -cl  ;
select -r root_geo ;
selectKey -clear ;
// 0 // 
select -r root_geo spine_A_geo spine_B_geo chest_geo l_clavicle_geo l_upArm_geo l_loArm_geo l_hand_geo r_clavicle_geo r_upArm_geo r_loArm_geo r_hand_geo neck_geo head_geo l_upLeg_geo l_loLeg_geo l_foot_geo l_toe_geo r_upLeg_geo r_loLeg_geo r_foot_geo r_toe_geo ;
selectKey -clear ;
// 0 // 
parent -w;
// Warning: line 0: Object, 'root_geo', skipped. It is already a child of the parent, 'world'. // 
// spine_A_geo spine_B_geo chest_geo l_clavicle_geo l_upArm_geo l_loArm_geo l_hand_geo r_clavicle_geo r_upArm_geo r_loArm_geo r_hand_geo neck_geo head_geo l_upLeg_geo l_loLeg_geo l_foot_geo l_toe_geo r_upLeg_geo r_loLeg_geo r_foot_geo r_toe_geo // 
select -r spine_A_geo ;
selectKey -clear ;
// 0 // 
select -r spine_A_geo spine_B_geo chest_geo l_clavicle_geo l_upArm_geo l_loArm_geo l_hand_geo r_clavicle_geo r_upArm_geo r_loArm_geo r_hand_geo neck_geo head_geo l_upLeg_geo l_loLeg_geo l_foot_geo l_toe_geo r_upLeg_geo r_loLeg_geo r_foot_geo r_toe_geo ;
selectKey -clear ;
// 0 // 
doGroup 0 1 1;
select -r group1 ;
selectKey -clear ;
// 0 // 
rename "group1" "geo_grp";
// geo_grp // 
select -cl  ;
select -r chest_geo ;
select -cl  ;
select -r l_loarm ;
select -tgl l_loArm_geo ;
select -r l_loArm_geo ;
select -cl  ;
select -r l_loarm ;
rotate -r -os -fo 0 0 48.687381 ;
// Undo: rotate -r -os -fo 0 0 48.687381 
select -cl  ;
select -r l_uparm ;
select -tgl l_upArm_geo ;
rotate -r -os -fo 0 0 32.189093 ;
// Undo: rotate -r -os -fo 0 0 32.189093 
select -cl  ;
select -r l_clavicle ;
select -tgl l_clavicle_geo ;
select -cl  ;
select -r l_clavicle ;
select -tgl l_clavicle_geo ;
SmoothBindSkin;
rotate -r -os -fo 0 -12.953006 0 ;
// Undo: rotate -r -os -fo 0 -12.953006 0 
select -cl  ;
select -r neck_jnt ;
select -cl  ;
select -r head_jnt ;
select -tgl head_geo ;
SmoothBindSkin;
select -cl  ;
select -r neck_jnt ;
rotate -r -os -fo -1.503318 -2.913664 -5.965762 ;
select -tgl neck_geo ;
SmoothBindSkin;
select -cl  ;
select -r chest_jnt ;
select -tgl chest_geo ;
SmoothBindSkin;
select -r r_clavicle ;
select -tgl r_clavicle_geo ;
SmoothBindSkin;
select -r r_uparm ;
select -tgl r_upArm_geo ;
SmoothBindSkin;
select -cl  ;
select -r r_loarm ;
select -tgl r_loArm_geo ;
SmoothBindSkin;
select -r r_wrist ;
select -tgl r_hand_geo ;
SmoothBindSkin;
select -r chest_geo ;
select -r spine_B_geo ;
select -r chest_jnt ;
select -r spineB_jnt ;
select -tgl spine_B_geo ;
SmoothBindSkin;
select -r spineA_jnt ;
select -tgl spine_A_geo ;
SmoothBindSkin;
select -r root_jnt ;
select -tgl root_geo ;
SmoothBindSkin;
select -r l_upleg ;
select -tgl l_upLeg_geo ;
SmoothBindSkin;
select -r l_loleg ;
select -tgl l_loLeg_geo ;
SmoothBindSkin;
select -r l_loLeg_geo ;
select -r l_foot ;
select -tgl l_foot_geo ;
SmoothBindSkin;
select -r l_loLeg_geo ;
select -r l_foot_geo ;
select -r l_toe_geo ;
select -cl  ;
// Undo: select -cl  
// Undo: select -r l_toe_geo 
select -r l_toe_geo ;
select -r l_loLeg_geo ;
select -r l_foot_geo ;
select -r l_ball ;
select -r r_upleg ;
select -tgl r_upLeg_geo ;
SmoothBindSkin;
select -r r_loleg ;
select -tgl r_loLeg_geo ;
SmoothBindSkin;
select -r r_foot ;
select -tgl r_foot_geo ;
SmoothBindSkin;
select -cl  ;
select -r l_ball ;
select -tgl l_toe_geo ;
SmoothBindSkin;
select -r r_ball ;
select -tgl r_toe_geo ;
SmoothBindSkin;
select -cl  ;
select -r bindPose1 ;
selectKey -clear ;
// 0 // 
select -r bindPose1 bindPose10 bindPose11 bindPose12 bindPose13 bindPose14 bindPose15 bindPose2 bindPose3 bindPose4 bindPose5 bindPose6 bindPose7 bindPose8 bindPose9 ;
selectKey -clear ;
// 0 // 
select -r head_geo ;
select -addFirst skinCluster5 ;
rename "skinCluster5" "head_geo_sCls";
// head_geo_sCls // 
select -r l_clavicle_geo ;
select -r neck_geo ;
select -addFirst skinCluster6 ;
rename "skinCluster6" "neck_geo_sCls";
// neck_geo_sCls // 
select -r l_clavicle_geo ;
select -addFirst skinCluster4 ;
rename "skinCluster4" "l_clavicle_geo_sCls";
// l_clavicle_geo_sCls // 
select -r l_upArm_geo ;
select -addFirst skinCluster3 ;
rename "skinCluster3" "l_upArm_geo_sCls";
// l_upArm_geo_sCls // 
select -r l_loArm_geo ;
select -addFirst skinCluster2 ;
rename "skinCluster2" "l_loArm_geo_sCls";
// l_loArm_geo_sCls // 
select -r l_hand_geo ;
select -addFirst l_hand_geo_sCls ;
select -r chest_geo ;
select -addFirst skinCluster7 ;
rename "skinCluster7" "chest_geo_sCls";
// chest_geo_sCls // 
select -r r_clavicle_geo ;
select -addFirst skinCluster8 ;
rename "skinCluster8" "r_clavicle_geo_sCls";
// r_clavicle_geo_sCls // 
select -r r_upArm_geo ;
select -addFirst skinCluster9 ;
rename "skinCluster9" "r_upArm_geo_sCls";
// r_upArm_geo_sCls // 
select -r r_loArm_geo ;
select -addFirst skinCluster10 ;
rename "skinCluster10" "r_loArm_geo_sCls";
// r_loArm_geo_sCls // 
select -r r_hand_geo ;
select -addFirst tweak11 ;
select -d tweak11 ;
select -addFirst skinCluster11 ;
rename "skinCluster11" "r_hand_geo_sCls";
// r_hand_geo_sCls // 
select -r spine_B_geo ;
select -addFirst skinCluster12 ;
rename "skinCluster12" "spine_B_geo_sCls";
// spine_B_geo_sCls // 
select -cl  ;
select -r root_geo spine_A_geo ;
select -addFirst skinCluster13 skinCluster14 ;
rename "skinCluster13" "spine_A_geo _";
// Warning: line 1: New name contains invalid characters. Illegal characters were converted to "_". // 
// spine_A_geo__ // 
rename "spine_A_geo__" "spine_A_geo_sCls";
// spine_A_geo_sCls // 
select -r root_geo ;
select -addFirst skinCluster14 ;
rename "skinCluster14" "root_geo_sCls";
// root_geo_sCls // 
select -r r_upLeg_geo ;
select -addFirst skinCluster18 ;
rename "skinCluster18" "r_upLeg_geo_sCls";
// r_upLeg_geo_sCls // 
select -r l_upLeg_geo ;
select -r spine_B_geo ;
select -r spine_A_geo ;
select -r root_geo ;
select -r spine_A_geo ;
select -r root_geo ;
select -r l_upLeg_geo ;
select -addFirst skinCluster15 ;
rename "skinCluster15" "l_upLeg_geo_sCls";
// l_upLeg_geo_sCls // 
select -r r_upLeg_geo ;
select -cl  ;
select -r l_loLeg_geo ;
select -addFirst skinCluster16 ;
rename "skinCluster16" "l_loLeg_geo_sCls";
// l_loLeg_geo_sCls // 
select -r r_loLeg_geo ;
select -addFirst skinCluster19 ;
rename "skinCluster19" "r_loLeg_geo_sCls";
// r_loLeg_geo_sCls // 
select -r r_foot_geo ;
select -addFirst skinCluster20 ;
rename "skinCluster20" "r_foot_geo_sCls";
// r_foot_geo_sCls // 
select -r r_toe_geo ;
select -addFirst skinCluster22 ;
rename "skinCluster22" "r_toe_geo_sCls";
// r_toe_geo_sCls // 
select -r l_foot_geo ;
select -addFirst skinCluster17 ;
rename "skinCluster17" "l_foot_geo_sCls";
// l_foot_geo_sCls // 
select -cl  ;
select -r l_loLeg_geo ;
select -cl  ;
select -r l_toe_geo ;
select -addFirst skinCluster21 ;
rename "skinCluster21" "l_toe_geo_sCls";
// l_toe_geo_sCls // 
select -cl  ;
select -r l_upLeg_geo ;
selectKey -clear ;
// 0 // 
select -cl  ;
select -r root_jnt ;
select -cl  ;
select -r spine_A_geo ;
selectKey -clear ;
// 0 // 
select -r spineA_jnt ;
selectKey -clear ;
// 0 // 
select -r root_jnt ;
selectKey -clear ;
// 0 // 
select -r root_jnt spineA_jnt spineB_jnt chest_jnt neck_jnt head_jnt l_clavicle l_uparm l_loarm l_wrist r_clavicle r_uparm r_loarm r_wrist l_upleg l_loleg l_foot l_ball l_toe r_upleg r_loleg r_foot r_ball r_toe ;
selectKey -clear ;
// 0 // 
select -cl  ;
select -r root_geo ;
select -cl  ;
select -r root_jnt ;
selectKey -clear ;
// 0 // 
move -r -os -wd 0 0 1.533417 ;
move -r -os -wd 0 7.571789 0 ;
// Undo: move -r -os -wd 0 7.571789 0 
move -r -os -wd 0 -19.063942 0 ;
// Undo: move -r -os -wd 0 -19.063942 0 
displaySmoothness -polygonObject 0;
select -cl  ;
// Undo: select -cl  
// Undo: DefaultQualityDisplay
// Undo: move -r -os -wd 0 0 1.533417 
select -cl  ;
// Undo: select -cl  
// Undo: select -r root_jnt 
// Undo: select -cl  
// Undo: select -r root_geo 
select -r head_jnt ;
selectKey -clear ;
// 0 // 
select -r chest_jnt ;
selectKey -clear ;
// 0 // 
select -cl  ;
select -r root_jnt ;
selectKey -clear ;
// 0 // 
select -r root_jnt spineA_jnt spineB_jnt chest_jnt neck_jnt head_jnt l_clavicle l_uparm l_loarm l_wrist r_clavicle r_uparm r_loarm r_wrist l_upleg l_loleg l_foot l_ball l_toe r_upleg r_loleg r_foot r_ball r_toe ;
selectKey -clear ;
// 0 // 
file -f -save  -options "v=0;";
// C:/Users/samha_000/Documents/Sam_Habib_B23/assets/Sams_r1_geo_Week4.ma // 
select -cl  ;
select -r root_geo ;
select -r root_jnt ;
setAttr "root_jnt.translateX" 0;
select -r spineA_jnt ;
selectKey -clear ;
// 0 // 
select -cl  ;
select -r chest_geo ;
select -cl  ;
circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0.01 -s 8 -ch 1; objectMoveCommand;
select -r root_jnt ;
selectKey -clear ;
// 0 // 
select -r nurbsCircle1 ;
doDelete;
circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0.01 -s 8 -ch 1; objectMoveCommand;
move -r -os -wd 0 18.219336 0 ;
select -r root_geo ;
select -r nurbsCircle1 ;
select -cl  ;
select -r nurbsCircle1 ;
select -cl  ;
select -r root_jnt ;
select -r nurbsCircle1 ;
select -r root_jnt ;
select -r root_jnt ;
select -r root_geo ;
select -r root_geo ;
select -r root_geo ;
select -cl  ;
select -r root_geo ;
select -r root_jnt ;
select -r nurbsCircle1 ;
select -r root_jnt ;
select -r nurbsCircle1 ;
move -r -os -wd 0 -0.0362232 0.0336167 ;
SnapToPoint; dR_enterForSnap;
select -cl  ;
select -r root_geo ;
select -cl  ;
select -r nurbsCircle1 ;
select -addFirst makeNurbCircle1 ;
select -r root_geo ;
select -cl  ;
select -r nurbsCircle1 ;
isolateSelect -state 1 modelPanel4;
select -r nurbsCircle1.cv[0:7] ;
isolateSelect -state 0 modelPanel4;
scale -ws -r -p 0cm 18.183113cm 0.0336167cm 4.363738 4.363738 4.363738 ;
scale -ws -r -p 0cm 18.183113cm 0.0336167cm 1.01116 1.01116 1.01116 ;
select -cl  ;
select -r root_geo ;
select -cl  ;
select -r nurbsCircle1 ;
select -r nurbsCircle1 ;
setAttr "nurbsCircle1.translateZ" 0;
setAttr "nurbsCircle1.translateX" 0;
setAttr "nurbsCircle1.translateY" 18.0;
setAttr "nurbsCircle1.translateY" 0;
select -r nurbsCircle1 ;
selectKey -clear ;
// 0 // 
doGroup 0 1 1;
select -r nurbsCircle1 ;
selectKey -clear ;
// 0 // 
rename "nurbsCircle1" "root_ctrl";
// root_ctrl // 
select -r group1 ;
selectKey -clear ;
// 0 // 
rename "group1" "root_offset";
// root_offset // 
select -r root_offset ;
selectKey -clear ;
// 0 // 
select -r root_geo ;
select -r root_offset ;
selectKey -clear ;
// 0 // 
move -r -os -wd 0 3.018162 0 ;
SnapToPoint; dR_enterForSnap;
select -r root_ctrl ;
selectKey -clear ;
// 0 // 
select -r root_offset ;
selectKey -clear ;
// 0 // 
move -r -os -wd 0 15.182369 0 ;
SnapToPoint; dR_enterForSnap;
move -r -os -wd 0 -0.0174178 0.0336167 ;
SnapToPoint; dR_enterForSnap;
select -r root_ctrl ;
selectKey -clear ;
// 0 // 
select -r root_ctrl root_offset geo_grp root_jnt ;
selectKey -clear ;
// 0 // 
select -r root_ctrl ;
selectKey -clear ;
// 0 // 
select -add root_jnt ;
doCreateParentConstraintArgList 1 { "1","0","0","0","0","0","0","0","1","","1" };
parentConstraint -mo -weight 1;
// root_jnt_parentConstraint1 // 
select -cl  ;
select -r root_ctrl ;
move -r -os -wd 4.06845 0 0 ;
move -r -os -wd 0 0 3.005307 ;
move -r -os -wd -5.631806 0 0 ;
setAttr "root_ctrl.translateZ" 0;
setAttr "root_ctrl.translateX" 0;
setAttr "root_ctrl.translateY" 0;
select -r root_ctrl ;
select -cl  ;
select -r root_ctrl ;
select -cl  ;
select -r root_ctrl ;
select -r root_offset ;
selectKey -clear ;
// 0 // 
select -r root_ctrl ;
selectKey -clear ;
// 0 // 
setAttr "root_ctrlShape.overrideEnabled" 1;
select -cl  ;
select -r root_ctrl ;
select -r root_ctrl ;
select -cl  ;
// Performing Incremental Save:
//   master file:    C:/Users/samha_000/Documents/Sam_Habib_B23/assets/Sams_r1_geo_Week4.ma
//   increment file: C:/Users/samha_000/Documents/Sam_Habib_B23/assets/incrementalSave/Sams_r1_geo_Week4.ma/Sams_r1_geo_Week4.0001.ma
file -force -save -options "v=0";
// C:/Users/samha_000/Documents/Sam_Habib_B23/assets/Sams_r1_geo_Week4.ma // 
select -r chest_geo ;
select -cl  ;
select -r spine_A_geo ;
select -r l_loArm_geo ;
select -cl  ;
select -r l_loArm_geo ;
select -cl  ;
select -r root_geo ;
select -r chest_geo ;
select -r head_geo ;
select -cl  ;
select -r root_geo ;
select -cl  ;
setToolTo CreatePolyCubeCtx;
polyCube -ch on -o on -w 8.729235 -h 8.729235 -d 8.729235 -cuv 4 ;
// Result: pCube1 polyCube1 // 
select -af polyCube1 ;
select -r pCube1 ;
# keyRotationTimeWithUI.py

import maya.cmds as cmds
import functools

def createUI(pWindowTitle, pApplyCallback):

    windowID = 'myWindowID'

    # Check to see if another window is activated already
    if cmds.window(windowID, exists = True):
        cmds.deleteUI(windowID)

    cmds.window(windowID, title = pWindowTitle, sizeable = True, resizeToFitChildren = True)

    cmds.rowColumnLayout( numberOfColumns = 3[(1,75), (2,75), (3,75)], columnOffset =[(1, 'right', 3) ] )

    cmds.text( label = 'Time Range: ')

    startTimeField = cmds.intField( value = cmds.playbackOptions(q = True, minTime = True))

    endTimeField = cmds.intField(value=cmds.playbackOptions(q = True, maxTime = True))

    cmds.text(label = 'Attribute: ')

    targetAttributeField = cmds.textField(text = "rotateY")

    cmds.separator(h = 10, style = 'none')

    cmds.text(label = 'Value Range: ')

    startValueField = cmds.intField(data = cmds.playpackOptions(q = True))

    endValueField = cmds.intField(data = cmds.playbackOptions(q = True))

    cmds.separator(h = 10, style = 'none')

    cmds.button(label = 'Apply', command = functools.partial(pApplyCallback, startTimeField, endTimeField, targetAttributeField, startValueField, endValueField))

    def cancelCallback(*pArgs):
        if cmds.window(windowID, exists = True):
            cmds.deleteUI(windowID)

    cmds.button(label = 'Cancel', command = cancelCallback)

    cmds.showWindow()

    def keyTransform(pObjectName, pStartTime, pEndTime, pTargetAttribute, pStartValue, pEndValue):

        cmds.cutKey(pObjectName, time = (pStartTime, pEndTime), attribute = pTargetAttribute)

        cmds.setKeyframe(pObjectName, time = pStartTime, attribute = pTargetAttribute, value = pStartValue)

        cmds.setKeyframe(pObjectName, time = pEndTime, attribute = pTargetAttribute, value = pEndValue)

        cmds.selectKey(pObjectName, time = (pStartTime, pEndTime), attribute = pTargetAttribute, keyframe = True)

        cmds.keyTangent(inTangentType = 'linear', outTangentType = 'linear')


    def applyCallback(pStartTimeField, pEndTimeField, pTargetAttributeField, pStartValueField, pEndValueField):
        # print 'Apply button pressed.'

        startTime = cmds.intField(pStartTimeField, query=True, value=True)

        endTime = cmds.intField(pEndTimeField, query=True, value=True)

        targetAttribute = cmds.textField(pTargetAttributeField, query=True, text=True)

        startValue = cmds.intField(pStartValueField, query=True, value=True)

        endValue = cmds.intField(pEndValueField, query=True, value=True)

        print
        'Start Time: %s' % (startTime)
        print
        'End Time: %s' % (endTime)
        print
        'Attribute: %s' % (targetAttribute)
        print
        'Start Value: %s' % (startValue)
        print
        'End Value: %s' % (endValue)
        
        selectionList = cmds.ls(selection=True, type='transform')

        for objectName in selectionList:
            keyTransform(objectName, startTime, endTime, targetAttribute, startValue, endValue)

    createUI('My Title', applyCallback)
select -r pCube1 ;
# keyRotationTimeWithUI.py

import maya.cmds as cmds
import functools


def createUI(pWindowTitle, pApplyCallback):
    windowID = 'myWindowID'

    # Check to see if another window is activated already
    if cmds.window(windowID, exists=True):
        cmds.deleteUI(windowID)

    cmds.window(windowID, title = pWindowTitle, sizeable = True, resizeToFitChildren = True )

    cmds.rowColumnLayout( numberOfColumns=3[ (1, 75), (2, 75), (3, 75) ], columnOffset=[ (1, 'right', 3) ] )

    cmds.text( label='Time Range: ' )

    startTimeField = cmds.intField( value=cmds.playbackOptions(q=True, minTime=True ) )

    endTimeField = cmds.intField( value=cmds.playbackOptions(q=True, maxTime=True ) )

    cmds.text( label='Attribute: ' )

    targetAttributeField = cmds.textField( text = "rotateY" )

    cmds.separator( h = 10, style = 'none' )

    cmds.text( label = 'Value Range: ' )
    startValueField = cmds.intField( data = cmds.playpackOptions( q = True ) )
    endValueField = cmds.intField( data=cmds.playbackOptions( q = True ) )

    cmds.separator( h = 10, style = 'none' )

    cmds.button( label = 'Apply', command = functools.partial(pApplyCallback, startTimeField, endTimeField, targetAttributeField, startValueField, endValueField))

    def cancelCallback(*pArgs):
        if cmds.window(windowID, exists = True):
            cmds.deleteUI(windowID)

    cmds.button(label='Cancel', command=cancelCallback)

    cmds.showWindow()

def keyTransform(pObjectName, pStartTime, pEndTime, pTargetAttribute, pStartValue, pEndValue):

    cmds.cutKey(pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute)

    cmds.setKeyframe(pObjectName, time=pStartTime, attribute=pTargetAttribute, value=pStartValue)

    cmds.setKeyframe(pObjectName, time=pEndTime, attribute=pTargetAttribute, value=pEndValue)

    cmds.selectKey(pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute, keyframe=True)

    cmds.keyTangent(inTangentType='linear', outTangentType='linear')

def applyCallback(pStartTimeField, pEndTimeField, pTargetAttributeField, pStartValueField, pEndValueField):
        # print 'Apply button pressed.'

    startTime = cmds.intField(pStartTimeField, query=True, value=True)

    endTime = cmds.intField(pEndTimeField, query=True, value=True)

    targetAttribute = cmds.textField(pTargetAttributeField, query=True, text=True)

    startValue = cmds.intField(pStartValueField, query=True, value=True)

    endValue = cmds.intField(pEndValueField, query=True, value=True)

    print
    'Start Time: %s' % (startTime)
    print
    'End Time: %s' % (endTime)
    print
    'Attribute: %s' % (targetAttribute)
    print
    'Start Value: %s' % (startValue)
    print
    'End Value: %s' % (endValue)

    selectionList = cmds.ls(selection=True, type='transform')

    for objectName in selectionList:
        keyTransform(objectName, startTime, endTime, targetAttribute, startValue, endValue)

createUI('My Title', applyCallback)
# Error: line 1: TypeError: file <maya console> line 16: 'int' object has no attribute '__getitem__' # 
// Warning: file: C:/Program Files/Autodesk/Maya2017/scripts/startup/scriptEditorPanel.mel line 1813: Could not find the specified string. // 
select -r pCube1 ;
# keyRotationTimeWithUI.py

import maya.cmds as cmds
import functools


def createUI(pWindowTitle, pApplyCallback):
    windowID = 'myWindowID'

    # Check to see if another window is activated already
    if cmds.window(windowID, exists=True):
        cmds.deleteUI(windowID)

    cmds.window(windowID, title = pWindowTitle, sizeable = True, resizeToFitChildren = True )

    cmds.rowColumnLayout( numberOfColumns = 3, columnWidth = [ (1, 75), (2, 75), (3, 75) ], columnOffset=[ (1, 'right', 3) ] )

    cmds.text( label='Time Range: ' )

    startTimeField = cmds.intField( value=cmds.playbackOptions(q=True, minTime=True ) )

    endTimeField = cmds.intField( value=cmds.playbackOptions(q=True, maxTime=True ) )

    cmds.text( label='Attribute: ' )

    targetAttributeField = cmds.textField( text = "rotateY" )

    cmds.separator( h = 10, style = 'none' )

    cmds.text( label = 'Value Range: ' )
    startValueField = cmds.intField( data = cmds.playpackOptions( q = True ) )
    endValueField = cmds.intField( data=cmds.playbackOptions( q = True ) )

    cmds.separator( h = 10, style = 'none' )

    cmds.button( label = 'Apply', command = functools.partial(pApplyCallback, startTimeField, endTimeField, targetAttributeField, startValueField, endValueField))

    def cancelCallback(*pArgs):
        if cmds.window(windowID, exists = True):
            cmds.deleteUI(windowID)

    cmds.button(label='Cancel', command=cancelCallback)

    cmds.showWindow()

def keyTransform(pObjectName, pStartTime, pEndTime, pTargetAttribute, pStartValue, pEndValue):

    cmds.cutKey(pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute)

    cmds.setKeyframe(pObjectName, time=pStartTime, attribute=pTargetAttribute, value=pStartValue)

    cmds.setKeyframe(pObjectName, time=pEndTime, attribute=pTargetAttribute, value=pEndValue)

    cmds.selectKey(pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute, keyframe=True)

    cmds.keyTangent(inTangentType='linear', outTangentType='linear')

def applyCallback(pStartTimeField, pEndTimeField, pTargetAttributeField, pStartValueField, pEndValueField):
        # print 'Apply button pressed.'

    startTime = cmds.intField(pStartTimeField, query=True, value=True)

    endTime = cmds.intField(pEndTimeField, query=True, value=True)

    targetAttribute = cmds.textField(pTargetAttributeField, query=True, text=True)

    startValue = cmds.intField(pStartValueField, query=True, value=True)

    endValue = cmds.intField(pEndValueField, query=True, value=True)

    print
    'Start Time: %s' % (startTime)
    print
    'End Time: %s' % (endTime)
    print
    'Attribute: %s' % (targetAttribute)
    print
    'Start Value: %s' % (startValue)
    print
    'End Value: %s' % (endValue)

    selectionList = cmds.ls(selection=True, type='transform')

    for objectName in selectionList:
        keyTransform(objectName, startTime, endTime, targetAttribute, startValue, endValue)

createUI('My Title', applyCallback)
# Error: line 1: AttributeError: file <maya console> line 31: 'module' object has no attribute 'playpackOptions' # 
# keyRotationTimeWithUI.py

import maya.cmds as cmds
import functools


def createUI(pWindowTitle, pApplyCallback):
    windowID = 'myWindowID'

    # Check to see if another window is activated already
    if cmds.window(windowID, exists=True):
        cmds.deleteUI(windowID)

    cmds.window(windowID, title = pWindowTitle, sizeable = True, resizeToFitChildren = True )

    cmds.rowColumnLayout( numberOfColumns = 3, columnWidth = [ (1, 75), (2, 75), (3, 75) ], columnOffset=[ (1, 'right', 3) ] )

    cmds.text( label='Time Range: ' )

    startTimeField = cmds.intField( value=cmds.playbackOptions(q=True, minTime=True ) )

    endTimeField = cmds.intField( value=cmds.playbackOptions(q=True, maxTime=True ) )

    cmds.text( label='Attribute: ' )

    targetAttributeField = cmds.textField( text = "rotateY" )

    cmds.separator( h = 10, style = 'none' )

    cmds.text( label = 'Value Range: ' )
    startValueField = cmds.intField( data = cmds.playbackOptions( q = True ) )
    endValueField = cmds.intField( data=cmds.playbackOptions( q = True ) )

    cmds.separator( h = 10, style = 'none' )

    cmds.button( label = 'Apply', command = functools.partial(pApplyCallback, startTimeField, endTimeField, targetAttributeField, startValueField, endValueField))

    def cancelCallback(*pArgs):
        if cmds.window(windowID, exists = True):
            cmds.deleteUI(windowID)

    cmds.button(label='Cancel', command=cancelCallback)

    cmds.showWindow()

def keyTransform(pObjectName, pStartTime, pEndTime, pTargetAttribute, pStartValue, pEndValue):

    cmds.cutKey(pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute)

    cmds.setKeyframe(pObjectName, time=pStartTime, attribute=pTargetAttribute, value=pStartValue)

    cmds.setKeyframe(pObjectName, time=pEndTime, attribute=pTargetAttribute, value=pEndValue)

    cmds.selectKey(pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute, keyframe=True)

    cmds.keyTangent(inTangentType='linear', outTangentType='linear')

def applyCallback(pStartTimeField, pEndTimeField, pTargetAttributeField, pStartValueField, pEndValueField):
        # print 'Apply button pressed.'

    startTime = cmds.intField(pStartTimeField, query=True, value=True)

    endTime = cmds.intField(pEndTimeField, query=True, value=True)

    targetAttribute = cmds.textField(pTargetAttributeField, query=True, text=True)

    startValue = cmds.intField(pStartValueField, query=True, value=True)

    endValue = cmds.intField(pEndValueField, query=True, value=True)

    print
    'Start Time: %s' % (startTime)
    print
    'End Time: %s' % (endTime)
    print
    'Attribute: %s' % (targetAttribute)
    print
    'Start Value: %s' % (startValue)
    print
    'End Value: %s' % (endValue)

    selectionList = cmds.ls(selection=True, type='transform')

    for objectName in selectionList:
        keyTransform(objectName, startTime, endTime, targetAttribute, startValue, endValue)

createUI('My Title', applyCallback)
# Error: line 1: TypeError: file <maya console> line 31: Invalid flag 'data' # 
select -r pCube1 ;
# keyRotationTimeWithUI.py

import maya.cmds as cmds
import functools


def createUI(pWindowTitle, pApplyCallback):
    windowID = 'myWindowID'

    # Check to see if another window is activated already
    if cmds.window(windowID, exists=True):
        cmds.deleteUI(windowID)

    cmds.window(windowID, title = pWindowTitle, sizeable = True, resizeToFitChildren = True )

    cmds.rowColumnLayout( numberOfColumns = 3, columnWidth = [ (1, 75), (2, 75), (3, 75) ], columnOffset=[ (1, 'right', 3) ] )

    cmds.text( label='Time Range: ' )

    startTimeField = cmds.intField( value=cmds.playbackOptions(q=True, minTime=True ) )

    endTimeField = cmds.intField( value=cmds.playbackOptions(q=True, maxTime=True ) )

    cmds.text( label='Attribute: ' )

    targetAttributeField = cmds.textField( text = "rotateY" )

    cmds.separator( h = 10, style = 'none' )

    cmds.text( label = 'Value Range: ' )
    startValueField = cmds.intField( value = cmds.playbackOptions( q = True ) )
    endValueField = cmds.intField( value = cmds.playbackOptions( q = True ) )

    cmds.separator( h = 10, style = 'none' )

    cmds.button( label = 'Apply', command = functools.partial(pApplyCallback, startTimeField, endTimeField, targetAttributeField, startValueField, endValueField))

    def cancelCallback(*pArgs):
        if cmds.window(windowID, exists = True):
            cmds.deleteUI(windowID)

    cmds.button(label='Cancel', command=cancelCallback)

    cmds.showWindow()

def keyTransform(pObjectName, pStartTime, pEndTime, pTargetAttribute, pStartValue, pEndValue):

    cmds.cutKey(pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute)

    cmds.setKeyframe(pObjectName, time=pStartTime, attribute=pTargetAttribute, value=pStartValue)

    cmds.setKeyframe(pObjectName, time=pEndTime, attribute=pTargetAttribute, value=pEndValue)

    cmds.selectKey(pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute, keyframe=True)

    cmds.keyTangent(inTangentType='linear', outTangentType='linear')

def applyCallback(pStartTimeField, pEndTimeField, pTargetAttributeField, pStartValueField, pEndValueField):
        # print 'Apply button pressed.'

    startTime = cmds.intField(pStartTimeField, query=True, value=True)

    endTime = cmds.intField(pEndTimeField, query=True, value=True)

    targetAttribute = cmds.textField(pTargetAttributeField, query=True, text=True)

    startValue = cmds.intField(pStartValueField, query=True, value=True)

    endValue = cmds.intField(pEndValueField, query=True, value=True)

    print
    'Start Time: %s' % (startTime)
    print
    'End Time: %s' % (endTime)
    print
    'Attribute: %s' % (targetAttribute)
    print
    'Start Value: %s' % (startValue)
    print
    'End Value: %s' % (endValue)

    selectionList = cmds.ls(selection=True, type='transform')

    for objectName in selectionList:
        keyTransform(objectName, startTime, endTime, targetAttribute, startValue, endValue)

createUI('My Title', applyCallback)
# Error: line 1: TypeError: file <maya console> line 31: Invalid arguments for flag 'value'.  Expected int, got NoneType # 
# keyRotationTimeWithUI.py

import maya.cmds as cmds
import functools


def createUI(pWindowTitle, pApplyCallback):
    windowID = 'myWindowID'

    # Check to see if another window is activated already
    if cmds.window(windowID, exists=True):
        cmds.deleteUI(windowID)

    cmds.window(windowID, title = pWindowTitle, sizeable = True, resizeToFitChildren = True )

    cmds.rowColumnLayout( numberOfColumns = 3, columnWidth = [ (1, 75), (2, 75), (3, 75) ], columnOffset=[ (1, 'right', 3) ] )

    cmds.text( label='Time Range: ' )

    startTimeField = cmds.intField( value = cmds.playbackOptions(q = True, minTime = True ) )

    endTimeField = cmds.intField( value = cmds.playbackOptions(q = True, maxTime = True ) )

    cmds.text( label='Attribute: ' )

    targetAttributeField = cmds.textField( text = "rotateY" )

    cmds.separator( h = 10, style = 'none' )

    cmds.text( label = 'Value Range: ' )
    startValueField = cmds.intField( value = cmds.playbackOptions( q = True, minTime = True ) )
    endValueField = cmds.intField( value = cmds.playbackOptions( q = True, maxTime = True ) )

    cmds.separator( h = 10, style = 'none' )

    cmds.button( label = 'Apply', command = functools.partial(pApplyCallback, startTimeField, endTimeField, targetAttributeField, startValueField, endValueField))

    def cancelCallback(*pArgs):
        if cmds.window(windowID, exists = True):
            cmds.deleteUI(windowID)

    cmds.button(label='Cancel', command=cancelCallback)

    cmds.showWindow()

def keyTransform(pObjectName, pStartTime, pEndTime, pTargetAttribute, pStartValue, pEndValue):

    cmds.cutKey(pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute)

    cmds.setKeyframe(pObjectName, time=pStartTime, attribute=pTargetAttribute, value=pStartValue)

    cmds.setKeyframe(pObjectName, time=pEndTime, attribute=pTargetAttribute, value=pEndValue)

    cmds.selectKey(pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute, keyframe=True)

    cmds.keyTangent(inTangentType='linear', outTangentType='linear')

def applyCallback(pStartTimeField, pEndTimeField, pTargetAttributeField, pStartValueField, pEndValueField):
        # print 'Apply button pressed.'

    startTime = cmds.intField(pStartTimeField, query=True, value=True)

    endTime = cmds.intField(pEndTimeField, query=True, value=True)

    targetAttribute = cmds.textField(pTargetAttributeField, query=True, text=True)

    startValue = cmds.intField(pStartValueField, query=True, value=True)

    endValue = cmds.intField(pEndValueField, query=True, value=True)

    print
    'Start Time: %s' % (startTime)
    print
    'End Time: %s' % (endTime)
    print
    'Attribute: %s' % (targetAttribute)
    print
    'Start Value: %s' % (startValue)
    print
    'End Value: %s' % (endValue)

    selectionList = cmds.ls(selection=True, type='transform')

    for objectName in selectionList:
        keyTransform(objectName, startTime, endTime, targetAttribute, startValue, endValue)

createUI('My Title', applyCallback)
# keyRotationTimeWithUI.py

import maya.cmds as cmds
import functools


def createUI(pWindowTitle, pApplyCallback):
    windowID = 'myWindowID'

    # Check to see if another window is activated already
    if cmds.window(windowID, exists=True):
        cmds.deleteUI(windowID)

    cmds.window(windowID, title = pWindowTitle, sizeable = True, resizeToFitChildren = True )

    cmds.rowColumnLayout( numberOfColumns = 3, columnWidth = [ (1, 75), (2, 75), (3, 75) ], columnOffset=[ (1, 'right', 3) ] )

    cmds.text( label='Time Range: ' )

    startTimeField = cmds.intField( value = cmds.playbackOptions(q = True, minTime = True ) )

    endTimeField = cmds.intField( value = cmds.playbackOptions(q = True, maxTime = True ) )

    cmds.text( label='Attribute: ' )

    targetAttributeField = cmds.textField( text = "rotateY" )

    cmds.separator( h = 10, style = 'none' )

    cmds.text( label = 'Value Range: ' )
    startValueField = cmds.intField( value = cmds.playbackOptions( q = True, minTime = True ) )
    endValueField = cmds.intField( value = cmds.playbackOptions( q = True, maxTime = True ) )

    cmds.separator( h = 10, style = 'none' )

    cmds.button( label = 'Apply', command = functools.partial(pApplyCallback, startTimeField, endTimeField, targetAttributeField, startValueField, endValueField))

    def cancelCallback(*pArgs):
        if cmds.window(windowID, exists = True):
            cmds.deleteUI(windowID)

    cmds.button(label='Cancel', command=cancelCallback)

    cmds.showWindow()

def keyTransform(pObjectName, pStartTime, pEndTime, pTargetAttribute, pStartValue, pEndValue):

    cmds.cutKey(pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute)

    cmds.setKeyframe(pObjectName, time=pStartTime, attribute=pTargetAttribute, value=pStartValue)

    cmds.setKeyframe(pObjectName, time=pEndTime, attribute=pTargetAttribute, value=pEndValue)

    cmds.selectKey(pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute, keyframe=True)

    cmds.keyTangent(inTangentType='linear', outTangentType='linear')

def applyCallback(pStartTimeField, pEndTimeField, pTargetAttributeField, pStartValueField, pEndValueField):
        # print 'Apply button pressed.'

    startTime = cmds.intField(pStartTimeField, query=True, value=True)

    endTime = cmds.intField(pEndTimeField, query=True, value=True)

    targetAttribute = cmds.textField(pTargetAttributeField, query=True, text=True)

    startValue = cmds.intField(pStartValueField, query=True, value=True)

    endValue = cmds.intField(pEndValueField, query=True, value=True)

    print
    'Start Time: %s' % (startTime)
    print
    'End Time: %s' % (endTime)
    print
    'Attribute: %s' % (targetAttribute)
    print
    'Start Value: %s' % (startValue)
    print
    'End Value: %s' % (endValue)

    selectionList = cmds.ls(selection=True, type='transform')

    for objectName in selectionList:
        keyTransform(objectName, startTime, endTime, targetAttribute, startValue, endValue)

createUI('My Title', applyCallback)
# Error: applyCallback() takes exactly 5 arguments (6 given) # 
# keyRotationTimeWithUI.py

import maya.cmds as cmds
import functools


def createUI(pWindowTitle, pApplyCallback):
    windowID = 'myWindowID'

    # Check to see if another window is activated already
    if cmds.window(windowID, exists=True):
        cmds.deleteUI(windowID)

    cmds.window(windowID, title = pWindowTitle, sizeable = True, resizeToFitChildren = True )

    cmds.rowColumnLayout( numberOfColumns = 3, columnWidth = [ (1, 75), (2, 75), (3, 75) ], columnOffset=[ (1, 'right', 3) ] )

    cmds.text( label='Time Range: ' )

    startTimeField = cmds.intField( value = cmds.playbackOptions(q = True, minTime = True ) )

    endTimeField = cmds.intField( value = cmds.playbackOptions(q = True, maxTime = True ) )

    cmds.text( label='Attribute: ' )

    targetAttributeField = cmds.textField( text = "rotateY" )

    cmds.separator( h = 10, style = 'none' )

    cmds.text( label = 'Value Range: ' )
    startValueField = cmds.intField( value = cmds.playbackOptions( q = True, minTime = True ) )
    endValueField = cmds.intField( value = cmds.playbackOptions( q = True, maxTime = True ) )

    cmds.separator( h = 10, style = 'none' )

    cmds.button( label = 'Apply', command = functools.partial(pApplyCallback, startTimeField, endTimeField, targetAttributeField, startValueField, endValueField))

    def cancelCallback(*pArgs):
        if cmds.window(windowID, exists = True):
            cmds.deleteUI(windowID)

    cmds.button(label='Cancel', command=cancelCallback)

    cmds.showWindow()

def keyTransform(pObjectName, pStartTime, pEndTime, pTargetAttribute, pStartValue, pEndValue):

    cmds.cutKey(pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute)

    cmds.setKeyframe(pObjectName, time=pStartTime, attribute=pTargetAttribute, value=pStartValue)

    cmds.setKeyframe(pObjectName, time=pEndTime, attribute=pTargetAttribute, value=pEndValue)

    cmds.selectKey(pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute, keyframe=True)

    cmds.keyTangent(inTangentType='linear', outTangentType='linear')

def applyCallback(pStartTimeField, pEndTimeField, pTargetAttributeField, pStartValueField, pEndValueField, *pArgs):
        # print 'Apply button pressed.'

    startTime = cmds.intField(pStartTimeField, query=True, value=True)

    endTime = cmds.intField(pEndTimeField, query=True, value=True)

    targetAttribute = cmds.textField(pTargetAttributeField, query=True, text=True)

    startValue = cmds.intField(pStartValueField, query=True, value=True)

    endValue = cmds.intField(pEndValueField, query=True, value=True)

    print
    'Start Time: %s' % (startTime)
    print
    'End Time: %s' % (endTime)
    print
    'Attribute: %s' % (targetAttribute)
    print
    'Start Value: %s' % (startValue)
    print
    'End Value: %s' % (endValue)

    selectionList = cmds.ls(selection=True, type='transform')

    for objectName in selectionList:
        keyTransform(objectName, startTime, endTime, targetAttribute, startValue, endValue)

createUI('My Title', applyCallback)





// Press the ESC key to stop playback. // 
currentTime 24 ;
currentTime 24 ;
playbackOptions -min 25 -max 48 ;
playbackOptions -min 25 -max 48 ;
// Press the ESC key to stop playback. // 
currentTime 145 ;
# keyRotationTimeWithUI.py

import maya.cmds as cmds
import functools


def createUI(pWindowTitle, pApplyCallback):
    windowID = 'myWindowID'

    # Check to see if another window is activated already
    if cmds.window(windowID, exists=True):
        cmds.deleteUI(windowID)

    cmds.window(windowID, title = pWindowTitle, sizeable = True, resizeToFitChildren = True )

    cmds.rowColumnLayout( numberOfColumns = 3, columnWidth = [ (1, 75), (2, 75), (3, 75) ], columnOffset=[ (1, 'right', 3) ] )

    cmds.text( label='Time Range: ' )

    startTimeField = cmds.intField( value = cmds.playbackOptions(q = True, minTime = True ) )

    endTimeField = cmds.intField( value = cmds.playbackOptions(q = True, maxTime = True ) )

    cmds.text( label='Attribute: ' )

    targetAttributeField = cmds.textField( text = "rotateY" )

    cmds.separator( h = 10, style = 'none' )

    cmds.text( label = 'Value Range: ' )
    startValueField = cmds.intField( value = cmds.playbackOptions( q = True, minTime = True ) )
    endValueField = cmds.intField( value = cmds.playbackOptions( q = True, maxTime = True ) )

    cmds.separator( h = 10, style = 'none' )

    cmds.button( label = 'Apply', command = functools.partial(pApplyCallback, startTimeField, endTimeField, targetAttributeField, startValueField, endValueField))

    def cancelCallback(*pArgs):
        if cmds.window(windowID, exists = True):
            cmds.deleteUI(windowID)

    cmds.button(label='Cancel', command=cancelCallback)

    cmds.showWindow()

def keyTransform(pObjectName, pStartTime, pEndTime, pTargetAttribute, pStartValue, pEndValue):

    cmds.cutKey(pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute)

    cmds.setKeyframe(pObjectName, time=pStartTime, attribute=pTargetAttribute, value=pStartValue)

    cmds.setKeyframe(pObjectName, time=pEndTime, attribute=pTargetAttribute, value=pEndValue)

    cmds.selectKey(pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute, keyframe=True)

    cmds.keyTangent(inTangentType='linear', outTangentType='linear')

def applyCallback(pStartTimeField, pEndTimeField, pTargetAttributeField, pStartValueField, pEndValueField, *pArgs):
        # print 'Apply button pressed.'

    startTime = cmds.intField(pStartTimeField, query=True, value=True)

    endTime = cmds.intField(pEndTimeField, query=True, value=True)

    targetAttribute = cmds.textField(pTargetAttributeField, query=True, text=True)

    startValue = cmds.intField(pStartValueField, query=True, value=True)

    endValue = cmds.intField(pEndValueField, query=True, value=True)

    print
    'Start Time: %s' % (startTime)
    print
    'End Time: %s' % (endTime)
    print
    'Attribute: %s' % (targetAttribute)
    print
    'Start Value: %s' % (startValue)
    print
    'End Value: %s' % (endValue)

    selectionList = cmds.ls(selection=True, type='transform')

    for objectName in selectionList:
        keyTransform(objectName, startTime, endTime, targetAttribute, startValue, endValue)

createUI('My Title', applyCallback)
# keyRotationTimeWithUI.py

import maya.cmds as cmds
import functools


def createUI(pWindowTitle, pApplyCallback):
    windowID = 'myWindowID'

    # Check to see if another window is activated already
    if cmds.window(windowID, exists=True):
        cmds.deleteUI(windowID)

    cmds.window(windowID, title = pWindowTitle, sizeable = True, resizeToFitChildren = True )

    cmds.rowColumnLayout( numberOfColumns = 3, columnWidth = [ (1, 75), (2, 75), (3, 75) ], columnOffset=[ (1, 'right', 3) ] )

    cmds.text( label='Time Range: ' )

    startTimeField = cmds.intField( value = cmds.playbackOptions(q = True, minTime = True ) )

    endTimeField = cmds.intField( value = cmds.playbackOptions(q = True, maxTime = True ) )

    cmds.text( label='Attribute: ' )

    targetAttributeField = cmds.textField( text = "rotateY" )

    cmds.separator( h = 10, style = 'none' )

    cmds.text( label = 'Value Range: ' )
    startValueField = cmds.intField( value = cmds.playbackOptions( q = True, minTime = True ) )
    endValueField = cmds.intField( value = cmds.playbackOptions( q = True, maxTime = True ) )

    cmds.separator( h = 10, style = 'none' )

    cmds.button( label = 'Apply', command = functools.partial(pApplyCallback, startTimeField, endTimeField, targetAttributeField, startValueField, endValueField))

    def cancelCallback(*pArgs):
        if cmds.window(windowID, exists = True):
            cmds.deleteUI(windowID)

    cmds.button(label='Cancel', command=cancelCallback)

    cmds.showWindow()

def keyTransform(pObjectName, pStartTime, pEndTime, pTargetAttribute, pStartValue, pEndValue):

    cmds.cutKey(pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute)

    cmds.setKeyframe(pObjectName, time=pStartTime, attribute=pTargetAttribute, value=pStartValue)

    cmds.setKeyframe(pObjectName, time=pEndTime, attribute=pTargetAttribute, value=pEndValue)

    cmds.selectKey(pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute, keyframe=True)

    cmds.keyTangent(inTangentType='linear', outTangentType='linear')

def applyCallback(pStartTimeField, pEndTimeField, pTargetAttributeField, pStartValueField, pEndValueField, *pArgs):
        # print 'Apply button pressed.'

    startTime = cmds.intField(pStartTimeField, query=True, value=True)

    endTime = cmds.intField(pEndTimeField, query=True, value=True)

    targetAttribute = cmds.textField(pTargetAttributeField, query=True, text=True)

    startValue = cmds.intField(pStartValueField, query=True, value=True)

    endValue = cmds.intField(pEndValueField, query=True, value=True)

    print
    'Start Time: %s' % (startTime)
    print
    'End Time: %s' % (endTime)
    print
    'Attribute: %s' % (targetAttribute)
    print
    'Start Value: %s' % (startValue)
    print
    'End Value: %s' % (endValue)

    selectionList = cmds.ls(selection=True, type='transform')

    for objectName in selectionList:
        keyTransform(objectName, startTime, endTime, targetAttribute, startValue, endValue)

createUI('My Title', applyCallback)





// Press the ESC key to stop playback. // 
currentTime 68 ;
# keyRotationTimeWithUI.py

import maya.cmds as cmds
import functools


def createUI(pWindowTitle, pApplyCallback):
    windowID = 'myWindowID'

    # Check to see if another window is activated already
    if cmds.window(windowID, exists=True):
        cmds.deleteUI(windowID)

    cmds.window(windowID, title = pWindowTitle, sizeable = True, resizeToFitChildren = True )

    cmds.rowColumnLayout( numberOfColumns = 3, columnWidth = [ (1, 75), (2, 75), (3, 75) ], columnOffset=[ (1, 'right', 3) ] )

    cmds.text( label='Time Range: ' )

    startTimeField = cmds.intField( value = cmds.playbackOptions(q = True, minTime = True ) )

    endTimeField = cmds.intField( value = cmds.playbackOptions(q = True, maxTime = True ) )

    cmds.text( label='Attribute: ' )

    targetAttributeField = cmds.textField( text = "rotateY" )

    cmds.separator( h = 10, style = 'none' )

    cmds.text( label = 'Value Range: ' )
    startValueField = cmds.intField( value = cmds.playbackOptions( q = True, minTime = True ) )
    endValueField = cmds.intField( value = cmds.playbackOptions( q = True, maxTime = True ) )

    cmds.separator( h = 10, style = 'none' )

    cmds.button( label = 'Apply', command = functools.partial(pApplyCallback, startTimeField, endTimeField, targetAttributeField, startValueField, endValueField))

    def cancelCallback(*pArgs):
        if cmds.window(windowID, exists = True):
            cmds.deleteUI(windowID)

    cmds.button(label='Cancel', command=cancelCallback)

    cmds.showWindow()

def keyTransform(pObjectName, pStartTime, pEndTime, pTargetAttribute, pStartValue, pEndValue):

    cmds.cutKey(pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute)

    cmds.setKeyframe(pObjectName, time=pStartTime, attribute=pTargetAttribute, value=pStartValue)

    cmds.setKeyframe(pObjectName, time=pEndTime, attribute=pTargetAttribute, value=pEndValue)

    cmds.selectKey(pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute, keyframe=True)

    cmds.keyTangent(inTangentType='linear', outTangentType='linear')

def applyCallback(pStartTimeField, pEndTimeField, pTargetAttributeField, pStartValueField, pEndValueField, *pArgs):
        # print 'Apply button pressed.'

    startTime = cmds.intField(pStartTimeField, query=True, value=True)

    endTime = cmds.intField(pEndTimeField, query=True, value=True)

    targetAttribute = cmds.textField(pTargetAttributeField, query=True, text=True)

    startValue = cmds.intField(pStartValueField, query=True, value=True)

    endValue = cmds.intField(pEndValueField, query=True, value=True)

    print
    'Start Time: %s' % (startTime)
    print
    'End Time: %s' % (endTime)
    print
    'Attribute: %s' % (targetAttribute)
    print
    'Start Value: %s' % (startValue)
    print
    'End Value: %s' % (endValue)

    selectionList = cmds.ls(selection=True, type='transform')

    for objectName in selectionList:
        keyTransform(objectName, startTime, endTime, targetAttribute, startValue, endValue)

createUI('My Title', applyCallback)





// Press the ESC key to stop playback. // 
currentTime 10 ;
# keyRotationTimeWithUI.py

import maya.cmds as cmds
import functools


def createUI(pWindowTitle, pApplyCallback):
    windowID = 'myWindowID'

    # Check to see if another window is activated already
    if cmds.window(windowID, exists=True):
        cmds.deleteUI(windowID)

    cmds.window(windowID, title = pWindowTitle, sizeable = True, resizeToFitChildren = True )

    cmds.rowColumnLayout( numberOfColumns = 3, columnWidth = [ (1, 75), (2, 75), (3, 75) ], columnOffset=[ (1, 'right', 3) ] )

    cmds.text( label='Time Range: ' )

    startTimeField = cmds.intField( value = cmds.playbackOptions(q = True, minTime = True ) )

    endTimeField = cmds.intField( value = cmds.playbackOptions(q = True, maxTime = True ) )

    cmds.text( label='Attribute: ' )

    targetAttributeField = cmds.textField( text = "rotateY" )

    cmds.separator( h = 10, style = 'none' )

    cmds.text( label = 'Value Range: ' )
    startValueField = cmds.intField( value = cmds.playbackOptions( q = True, minTime = True ) )
    endValueField = cmds.intField( value = cmds.playbackOptions( q = True, maxTime = True ) )

    cmds.separator( h = 10, style = 'none' )

    cmds.button( label = 'Apply', command = functools.partial(pApplyCallback, startTimeField, endTimeField, targetAttributeField, startValueField, endValueField))

    def cancelCallback(*pArgs):
        if cmds.window(windowID, exists = True):
            cmds.deleteUI(windowID)

    cmds.button(label='Cancel', command=cancelCallback)

    cmds.showWindow()

def keyTransform(pObjectName, pStartTime, pEndTime, pTargetAttribute, pStartValue, pEndValue):

    cmds.cutKey(pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute)

    cmds.setKeyframe(pObjectName, time=pStartTime, attribute=pTargetAttribute, value=pStartValue)

    cmds.setKeyframe(pObjectName, time=pEndTime, attribute=pTargetAttribute, value=pEndValue)

    cmds.selectKey(pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute, keyframe=True)

    cmds.keyTangent(inTangentType='linear', outTangentType='linear')

def applyCallback(pStartTimeField, pEndTimeField, pTargetAttributeField, pStartValueField, pEndValueField, *pArgs):
        # print 'Apply button pressed.'

    startTime = cmds.intField(pStartTimeField, query=True, value=True)

    endTime = cmds.intField(pEndTimeField, query=True, value=True)

    targetAttribute = cmds.textField(pTargetAttributeField, query=True, text=True)

    startValue = cmds.intField(pStartValueField, query=True, value=True)

    endValue = cmds.intField(pEndValueField, query=True, value=True)

    print
    'Start Time: %s' % (startTime)
    print
    'End Time: %s' % (endTime)
    print
    'Attribute: %s' % (targetAttribute)
    print
    'Start Value: %s' % (startValue)
    print
    'End Value: %s' % (endValue)

    selectionList = cmds.ls(selection=True, type='transform')

    for objectName in selectionList:
        keyTransform(objectName, startTime, endTime, targetAttribute, startValue, endValue)

createUI('My Title', applyCallback)





// Press the ESC key to stop playback. // 
currentTime 114 ;
# keyRotationTimeWithUI.py

import maya.cmds as cmds
import functools


def createUI(pWindowTitle, pApplyCallback):
    windowID = 'myWindowID'

    # Check to see if another window is activated already
    if cmds.window(windowID, exists=True):
        cmds.deleteUI(windowID)

    cmds.window(windowID, title = pWindowTitle, sizeable = True, resizeToFitChildren = True )

    cmds.rowColumnLayout( numberOfColumns = 3, columnWidth = [ (1, 75), (2, 75), (3, 75) ], columnOffset=[ (1, 'right', 3) ] )

    cmds.text( label='Time Range: ' )

    startTimeField = cmds.intField( value = cmds.playbackOptions(q = True, minTime = True ) )

    endTimeField = cmds.intField( value = cmds.playbackOptions(q = True, maxTime = True ) )

    cmds.text( label='Attribute: ' )

    targetAttributeField = cmds.textField( text = "rotateY" )

    cmds.separator( h = 10, style = 'none' )

    cmds.text( label = 'Value Range: ' )
    startValueField = cmds.intField( value = cmds.playbackOptions( q = True, animationStartTime = 0 ) )
    endValueField = cmds.intField( value = cmds.playbackOptions( q = True, animationEndTime = 360 ) )

    cmds.separator( h = 10, style = 'none' )

    cmds.button( label = 'Apply', command = functools.partial(pApplyCallback, startTimeField, endTimeField, targetAttributeField, startValueField, endValueField))

    def cancelCallback(*pArgs):
        if cmds.window(windowID, exists = True):
            cmds.deleteUI(windowID)

    cmds.button(label='Cancel', command=cancelCallback)

    cmds.showWindow()

def keyTransform(pObjectName, pStartTime, pEndTime, pTargetAttribute, pStartValue, pEndValue):

    cmds.cutKey(pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute)

    cmds.setKeyframe(pObjectName, time=pStartTime, attribute=pTargetAttribute, value=pStartValue)

    cmds.setKeyframe(pObjectName, time=pEndTime, attribute=pTargetAttribute, value=pEndValue)

    cmds.selectKey(pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute, keyframe=True)

    cmds.keyTangent(inTangentType='linear', outTangentType='linear')

def applyCallback(pStartTimeField, pEndTimeField, pTargetAttributeField, pStartValueField, pEndValueField, *pArgs):
        # print 'Apply button pressed.'

    startTime = cmds.intField(pStartTimeField, query=True, value=True)

    endTime = cmds.intField(pEndTimeField, query=True, value=True)

    targetAttribute = cmds.textField(pTargetAttributeField, query=True, text=True)

    startValue = cmds.intField(pStartValueField, query=True, value=True)

    endValue = cmds.intField(pEndValueField, query=True, value=True)

    print
    'Start Time: %s' % (startTime)
    print
    'End Time: %s' % (endTime)
    print
    'Attribute: %s' % (targetAttribute)
    print
    'Start Value: %s' % (startValue)
    print
    'End Value: %s' % (endValue)

    selectionList = cmds.ls(selection=True, type='transform')

    for objectName in selectionList:
        keyTransform(objectName, startTime, endTime, targetAttribute, startValue, endValue)

createUI('My Title', applyCallback)
# keyRotationTimeWithUI.py

import maya.cmds as cmds
import functools


def createUI(pWindowTitle, pApplyCallback):
    windowID = 'myWindowID'

    # Check to see if another window is activated already
    if cmds.window(windowID, exists=True):
        cmds.deleteUI(windowID)

    cmds.window(windowID, title = pWindowTitle, sizeable = True, resizeToFitChildren = True )

    cmds.rowColumnLayout( numberOfColumns = 3, columnWidth = [ (1, 75), (2, 75), (3, 75) ], columnOffset=[ (1, 'right', 3) ] )

    cmds.text( label='Time Range: ' )

    startTimeField = cmds.intField( value = cmds.playbackOptions(q = True, minTime = True ) )

    endTimeField = cmds.intField( value = cmds.playbackOptions(q = True, maxTime = True ) )

    cmds.text( label='Attribute: ' )

    targetAttributeField = cmds.textField( text = "rotateY" )

    cmds.separator( h = 10, style = 'none' )

    cmds.text( label = 'Value Range: ' )
    startValueField = cmds.intField( value = cmds.playbackOptions( q = True, animationStartTime = 0 ) )
    endValueField = cmds.intField( value = cmds.playbackOptions( q = True, animationEndTime = 360 ) )

    cmds.separator( h = 10, style = 'none' )

    cmds.button( label = 'Apply', command = functools.partial(pApplyCallback, startTimeField, endTimeField, targetAttributeField, startValueField, endValueField))

    def cancelCallback(*pArgs):
        if cmds.window(windowID, exists = True):
            cmds.deleteUI(windowID)

    cmds.button(label='Cancel', command=cancelCallback)

    cmds.showWindow()

def keyTransform(pObjectName, pStartTime, pEndTime, pTargetAttribute, pStartValue, pEndValue):

    cmds.cutKey(pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute)

    cmds.setKeyframe(pObjectName, time=pStartTime, attribute=pTargetAttribute, value=pStartValue)

    cmds.setKeyframe(pObjectName, time=pEndTime, attribute=pTargetAttribute, value=pEndValue)

    cmds.selectKey(pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute, keyframe=True)

    cmds.keyTangent(inTangentType='linear', outTangentType='linear')

def applyCallback(pStartTimeField, pEndTimeField, pTargetAttributeField, pStartValueField, pEndValueField, *pArgs):
        # print 'Apply button pressed.'

    startTime = cmds.intField(pStartTimeField, query=True, value=True)

    endTime = cmds.intField(pEndTimeField, query=True, value=True)

    targetAttribute = cmds.textField(pTargetAttributeField, query=True, text=True)

    startValue = cmds.intField(pStartValueField, query=True, value=True)

    endValue = cmds.intField(pEndValueField, query=True, value=True)

    print
    'Start Time: %s' % (startTime)
    print
    'End Time: %s' % (endTime)
    print
    'Attribute: %s' % (targetAttribute)
    print
    'Start Value: %s' % (startValue)
    print
    'End Value: %s' % (endValue)

    selectionList = cmds.ls(selection=True, type='transform')

    for objectName in selectionList:
        keyTransform(objectName, startTime, endTime, targetAttribute, startValue, endValue)

createUI('My Title', applyCallback)
# keyRotationTimeWithUI.py

import maya.cmds as cmds
import functools


def createUI(pWindowTitle, pApplyCallback):
    windowID = 'myWindowID'

    # Check to see if another window is activated already
    if cmds.window(windowID, exists=True):
        cmds.deleteUI(windowID)

    cmds.window(windowID, title = pWindowTitle, sizeable = True, resizeToFitChildren = True )

    cmds.rowColumnLayout( numberOfColumns = 3, columnWidth = [ (1, 75), (2, 75), (3, 75) ], columnOffset=[ (1, 'right', 3) ] )

    cmds.text( label='Time Range: ' )

    startTimeField = cmds.intField( value = cmds.playbackOptions(q = True, minTime = True ) )

    endTimeField = cmds.intField( value = cmds.playbackOptions(q = True, maxTime = True ) )

    cmds.text( label='Attribute: ' )

    targetAttributeField = cmds.textField( text = "rotateY" )

    cmds.separator( h = 10, style = 'none' )

    cmds.text( label = 'Value Range: ' )
    startValueField = cmds.intField( value = cmds.playbackOptions( q = True, minTime = 0 ) )
    endValueField = cmds.intField( value = cmds.playbackOptions( q = True, maxTime = 360 ) )

    cmds.separator( h = 10, style = 'none' )

    cmds.button( label = 'Apply', command = functools.partial(pApplyCallback, startTimeField, endTimeField, targetAttributeField, startValueField, endValueField))

    def cancelCallback(*pArgs):
        if cmds.window(windowID, exists = True):
            cmds.deleteUI(windowID)

    cmds.button(label='Cancel', command=cancelCallback)

    cmds.showWindow()

def keyTransform(pObjectName, pStartTime, pEndTime, pTargetAttribute, pStartValue, pEndValue):

    cmds.cutKey(pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute)

    cmds.setKeyframe(pObjectName, time=pStartTime, attribute=pTargetAttribute, value=pStartValue)

    cmds.setKeyframe(pObjectName, time=pEndTime, attribute=pTargetAttribute, value=pEndValue)

    cmds.selectKey(pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute, keyframe=True)

    cmds.keyTangent(inTangentType='linear', outTangentType='linear')

def applyCallback(pStartTimeField, pEndTimeField, pTargetAttributeField, pStartValueField, pEndValueField, *pArgs):
        # print 'Apply button pressed.'

    startTime = cmds.intField(pStartTimeField, query=True, value=True)

    endTime = cmds.intField(pEndTimeField, query=True, value=True)

    targetAttribute = cmds.textField(pTargetAttributeField, query=True, text=True)

    startValue = cmds.intField(pStartValueField, query=True, value=True)

    endValue = cmds.intField(pEndValueField, query=True, value=True)

    print
    'Start Time: %s' % (startTime)
    print
    'End Time: %s' % (endTime)
    print
    'Attribute: %s' % (targetAttribute)
    print
    'Start Value: %s' % (startValue)
    print
    'End Value: %s' % (endValue)

    selectionList = cmds.ls(selection=True, type='transform')

    for objectName in selectionList:
        keyTransform(objectName, startTime, endTime, targetAttribute, startValue, endValue)

createUI('My Title', applyCallback)





# keyRotationTimeWithUI.py

import maya.cmds as cmds
import functools


def createUI(pWindowTitle, pApplyCallback):
    windowID = 'myWindowID'

    # Check to see if another window is activated already
    if cmds.window(windowID, exists=True):
        cmds.deleteUI(windowID)

    cmds.window(windowID, title = pWindowTitle, sizeable = True, resizeToFitChildren = True )

    cmds.rowColumnLayout( numberOfColumns = 3, columnWidth = [ (1, 75), (2, 75), (3, 75) ], columnOffset=[ (1, 'right', 3) ] )

    cmds.text( label='Time Range: ' )

    startTimeField = cmds.intField( value = cmds.playbackOptions(q = True, minTime = True ) )

    endTimeField = cmds.intField( value = cmds.playbackOptions(q = True, maxTime = True ) )

    cmds.text( label='Attribute: ' )

    targetAttributeField = cmds.textField( text = "rotateY" )

    cmds.separator( h = 10, style = 'none' )

    cmds.text( label = 'Value Range: ' )
    startValueField = cmds.intField( value = cmds.playbackOptions( q = True, minTime = 0 ) )
    endValueField = cmds.intField( value = cmds.playbackOptions( q = True, maxTime = 360 ) )

    cmds.separator( h = 10, style = 'none' )

    cmds.button( label = 'Apply', command = functools.partial(pApplyCallback, startTimeField, endTimeField, targetAttributeField, startValueField, endValueField))

    def cancelCallback(*pArgs):
        if cmds.window(windowID, exists = True):
            cmds.deleteUI(windowID)

    cmds.button(label='Cancel', command=cancelCallback)

    cmds.showWindow()

def keyTransform(pObjectName, pStartTime, pEndTime, pTargetAttribute, pStartValue, pEndValue):

    cmds.cutKey(pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute)

    cmds.setKeyframe(pObjectName, time=pStartTime, attribute=pTargetAttribute, value=pStartValue)

    cmds.setKeyframe(pObjectName, time=pEndTime, attribute=pTargetAttribute, value=pEndValue)

    cmds.selectKey(pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute, keyframe=True)

    cmds.keyTangent(inTangentType='linear', outTangentType='linear')

def applyCallback(pStartTimeField, pEndTimeField, pTargetAttributeField, pStartValueField, pEndValueField, *pArgs):
        # print 'Apply button pressed.'

    startTime = cmds.intField(pStartTimeField, query=True, value=True)

    endTime = cmds.intField(pEndTimeField, query=True, value=True)

    targetAttribute = cmds.textField(pTargetAttributeField, query=True, text=True)

    startValue = cmds.intField(pStartValueField, query=True, value=True)

    endValue = cmds.intField(pEndValueField, query=True, value=True)

    print
    'Start Time: %s' % (startTime)
    print
    'End Time: %s' % (endTime)
    print
    'Attribute: %s' % (targetAttribute)
    print
    'Start Value: %s' % (startValue)
    print
    'End Value: %s' % (endValue)

    selectionList = cmds.ls(selection=True, type='transform')

    for objectName in selectionList:
        keyTransform(objectName, startTime, endTime, targetAttribute, startValue, endValue)

createUI('My Title', applyCallback)
// Press the ESC key to stop playback. // 
currentTime 163 ;
# keyRotationTimeWithUI.py

import maya.cmds as cmds
import functools


def createUI(pWindowTitle, pApplyCallback):
    windowID = 'myWindowID'

    # Check to see if another window is activated already
    if cmds.window(windowID, exists=True):
        cmds.deleteUI(windowID)

    cmds.window(windowID, title = pWindowTitle, sizeable = True, resizeToFitChildren = True )

    cmds.rowColumnLayout( numberOfColumns = 3, columnWidth = [ (1, 75), (2, 75), (3, 75) ], columnOffset=[ (1, 'right', 3) ] )

    cmds.text( label='Time Range: ' )

    startTimeField = cmds.intField( 0 ) )

    endTimeField = cmds.intField( 360 ) )

    cmds.text( label='Attribute: ' )

    targetAttributeField = cmds.textField( text = "rotateY" )

    cmds.separator( h = 10, style = 'none' )

    cmds.text( label = 'Value Range: ' )
    startValueField = cmds.intField( value = cmds.playbackOptions( q = True, minTime = 0 ) )
    endValueField = cmds.intField( value = cmds.playbackOptions( q = True, maxTime = 360 ) )

    cmds.separator( h = 10, style = 'none' )

    cmds.button( label = 'Apply', command = functools.partial(pApplyCallback, startTimeField, endTimeField, targetAttributeField, startValueField, endValueField))

    def cancelCallback(*pArgs):
        if cmds.window(windowID, exists = True):
            cmds.deleteUI(windowID)

    cmds.button(label='Cancel', command=cancelCallback)

    cmds.showWindow()

def keyTransform(pObjectName, pStartTime, pEndTime, pTargetAttribute, pStartValue, pEndValue):

    cmds.cutKey(pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute)

    cmds.setKeyframe(pObjectName, time=pStartTime, attribute=pTargetAttribute, value=pStartValue)

    cmds.setKeyframe(pObjectName, time=pEndTime, attribute=pTargetAttribute, value=pEndValue)

    cmds.selectKey(pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute, keyframe=True)

    cmds.keyTangent(inTangentType='linear', outTangentType='linear')

def applyCallback(pStartTimeField, pEndTimeField, pTargetAttributeField, pStartValueField, pEndValueField, *pArgs):
        # print 'Apply button pressed.'

    startTime = cmds.intField(pStartTimeField, query=True, value=True)

    endTime = cmds.intField(pEndTimeField, query=True, value=True)

    targetAttribute = cmds.textField(pTargetAttributeField, query=True, text=True)

    startValue = cmds.intField(pStartValueField, query=True, value=True)

    endValue = cmds.intField(pEndValueField, query=True, value=True)

    print
    'Start Time: %s' % (startTime)
    print
    'End Time: %s' % (endTime)
    print
    'Attribute: %s' % (targetAttribute)
    print
    'Start Value: %s' % (startValue)
    print
    'End Value: %s' % (endValue)

    selectionList = cmds.ls(selection=True, type='transform')

    for objectName in selectionList:
        keyTransform(objectName, startTime, endTime, targetAttribute, startValue, endValue)

createUI('My Title', applyCallback)
# Error: line 1: invalid syntax # 
# keyRotationTimeWithUI.py

import maya.cmds as cmds
import functools


def createUI(pWindowTitle, pApplyCallback):
    windowID = 'myWindowID'

    # Check to see if another window is activated already
    if cmds.window(windowID, exists=True):
        cmds.deleteUI(windowID)

    cmds.window(windowID, title = pWindowTitle, sizeable = True, resizeToFitChildren = True )

    cmds.rowColumnLayout( numberOfColumns = 3, columnWidth = [ (1, 75), (2, 75), (3, 75) ], columnOffset=[ (1, 'right', 3) ] )

    cmds.text( label='Time Range: ' )

    startTimeField = cmds.intField( 0 )

    endTimeField = cmds.intField( 360 )

    cmds.text( label='Attribute: ' )

    targetAttributeField = cmds.textField( text = "rotateY" )

    cmds.separator( h = 10, style = 'none' )

    cmds.text( label = 'Value Range: ' )
    startValueField = cmds.intField( value = cmds.playbackOptions( q = True, minTime = 0 ) )
    endValueField = cmds.intField( value = cmds.playbackOptions( q = True, maxTime = 360 ) )

    cmds.separator( h = 10, style = 'none' )

    cmds.button( label = 'Apply', command = functools.partial(pApplyCallback, startTimeField, endTimeField, targetAttributeField, startValueField, endValueField))

    def cancelCallback(*pArgs):
        if cmds.window(windowID, exists = True):
            cmds.deleteUI(windowID)

    cmds.button(label='Cancel', command=cancelCallback)

    cmds.showWindow()

def keyTransform(pObjectName, pStartTime, pEndTime, pTargetAttribute, pStartValue, pEndValue):

    cmds.cutKey(pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute)

    cmds.setKeyframe(pObjectName, time=pStartTime, attribute=pTargetAttribute, value=pStartValue)

    cmds.setKeyframe(pObjectName, time=pEndTime, attribute=pTargetAttribute, value=pEndValue)

    cmds.selectKey(pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute, keyframe=True)

    cmds.keyTangent(inTangentType='linear', outTangentType='linear')

def applyCallback(pStartTimeField, pEndTimeField, pTargetAttributeField, pStartValueField, pEndValueField, *pArgs):
        # print 'Apply button pressed.'

    startTime = cmds.intField(pStartTimeField, query=True, value=True)

    endTime = cmds.intField(pEndTimeField, query=True, value=True)

    targetAttribute = cmds.textField(pTargetAttributeField, query=True, text=True)

    startValue = cmds.intField(pStartValueField, query=True, value=True)

    endValue = cmds.intField(pEndValueField, query=True, value=True)

    print
    'Start Time: %s' % (startTime)
    print
    'End Time: %s' % (endTime)
    print
    'Attribute: %s' % (targetAttribute)
    print
    'Start Value: %s' % (startValue)
    print
    'End Value: %s' % (endValue)

    selectionList = cmds.ls(selection=True, type='transform')

    for objectName in selectionList:
        keyTransform(objectName, startTime, endTime, targetAttribute, startValue, endValue)

createUI('My Title', applyCallback)
# keyRotationTimeWithUI.py

import maya.cmds as cmds
import functools


def createUI(pWindowTitle, pApplyCallback):
    windowID = 'myWindowID'

    # Check to see if another window is activated already
    if cmds.window(windowID, exists=True):
        cmds.deleteUI(windowID)

    cmds.window(windowID, title = pWindowTitle, sizeable = True, resizeToFitChildren = True )

    cmds.rowColumnLayout( numberOfColumns = 3, columnWidth = [ (1, 75), (2, 75), (3, 75) ], columnOffset=[ (1, 'right', 3) ] )

    cmds.text( label='Time Range: ' )

    startTimeField = cmds.intField( value = cmds.playbackOptions(q = True, minTime = True ) )

    endTimeField = cmds.intField( value = cmds.playbackOptions(q = True, maxTime = True ) )

    cmds.text( label='Attribute: ' )

    targetAttributeField = cmds.textField( text = "rotateY" )

    cmds.separator( h = 10, style = 'none' )

    cmds.text( label = 'Value Range: ' )
    startValueField = cmds.intField( value = 0 )
    endValueField = cmds.intField( value = 360 )

    cmds.separator( h = 10, style = 'none' )

    cmds.button( label = 'Apply', command = functools.partial(pApplyCallback, startTimeField, endTimeField, targetAttributeField, startValueField, endValueField))

    def cancelCallback(*pArgs):
        if cmds.window(windowID, exists = True):
            cmds.deleteUI(windowID)

    cmds.button(label='Cancel', command=cancelCallback)

    cmds.showWindow()

def keyTransform(pObjectName, pStartTime, pEndTime, pTargetAttribute, pStartValue, pEndValue):

    cmds.cutKey(pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute)

    cmds.setKeyframe(pObjectName, time=pStartTime, attribute=pTargetAttribute, value=pStartValue)

    cmds.setKeyframe(pObjectName, time=pEndTime, attribute=pTargetAttribute, value=pEndValue)

    cmds.selectKey(pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute, keyframe=True)

    cmds.keyTangent(inTangentType='linear', outTangentType='linear')

def applyCallback(pStartTimeField, pEndTimeField, pTargetAttributeField, pStartValueField, pEndValueField, *pArgs):
        # print 'Apply button pressed.'

    startTime = cmds.intField(pStartTimeField, query=True, value=True)

    endTime = cmds.intField(pEndTimeField, query=True, value=True)

    targetAttribute = cmds.textField(pTargetAttributeField, query=True, text=True)

    startValue = cmds.intField(pStartValueField, query=True, value=True)

    endValue = cmds.intField(pEndValueField, query=True, value=True)

    print
    'Start Time: %s' % (startTime)
    print
    'End Time: %s' % (endTime)
    print
    'Attribute: %s' % (targetAttribute)
    print
    'Start Value: %s' % (startValue)
    print
    'End Value: %s' % (endValue)

    selectionList = cmds.ls(selection=True, type='transform')

    for objectName in selectionList:
        keyTransform(objectName, startTime, endTime, targetAttribute, startValue, endValue)

createUI('My Title', applyCallback)





// Press the ESC key to stop playback. // 
currentTime 68 ;
