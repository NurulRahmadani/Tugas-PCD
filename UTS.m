function varargout = UTS(varargin)
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @UTS_OpeningFcn, ...
                   'gui_OutputFcn',  @UTS_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
function UTS_OpeningFcn(hObject, eventdata, handles, varargin)
handles.output = hObject;

guidata(hObject, handles);

function varargout = UTS_OutputFcn(hObject, eventdata, handles) 
varargout{1} = handles.output;

function pushbutton1_Callback(hObject, eventdata, handles)
[filename, pathname] = uigetfile({'.jpeg','.jpsg'});

citra1 = imread ([pathname, filename]);
axes(handles.axes1);
imshow(citra1);
[tinggiA, lebarA] = size(citra1);

for baris=2 : tinggiA-1
    for kolom=2 : lebarA-1
        dataA = [citra1(baris-1, kolom-1) citra1(baris-1, kolom) citra1(baris-1, kolom+1)  ...
              citra1(baris, kolom-1) citra1(baris, kolom) citra1(baris, kolom+1)  ...
              citra1(baris+1, kolom-1) citra1(baris+1, kolom) citra1(baris+1, kolom+1)];
        
        for i=1 : 8
            for j=i+1 : 9
                if dataA(i) > dataA(j)
                    tmpA = dataA(i);
                    dataA(i) = dataA(j);
                    dataA(j) = tmpA;
                end
            end
        end 
        
        citra2(baris, kolom) = dataA(5);
    end
end
axes(handles.axes2);
imshow(citra2);