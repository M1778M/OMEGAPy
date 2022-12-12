// Includes [C Standard Libraries]
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>
// Defines Variables&Types
#define OMG_MAX_OBJSIZE (1024*1024*50)
#define _OMGINT_T 1
#define _OMGFLOAT_T 2
#define _OMGLIST_T 3
#define _OMGTUPLE_T 4
#define _OMGDICT_T 5
#define _OMGSET_T 6
#define _OMGBOOL_T 7
#define _OMGNONE_T 8
#define _OMGBYTE_T 9
#define _OMGTYPE_T 0
#define _OMGDEC_T 11
#define _OMGCLASS_T 12
#define _OMGUDC_T 13
#define _OMGFUNC_T 14
#define _OMGINT_N "oInt"
#define _OMGFLOAT_N "oFloat"
#define _OMGLIST_N "oList"
#define _OMGTUPLE_N "oTuple"
#define _OMGDICT_N "oDict"
#define _OMGSET_N "oSet"
#define _OMGBOOL_N "oBool"
#define _OMGNONE_N "oNone"
#define _OMGBYTE_N "oByte"
#define _OMGTYPE_N "oType"
#define _OMGDEC_N "Dec_v"
#define _OMGCLASS_N "oClass"
#define _OMGUDC_N "udc"
#define _OMGFUNC_N "oFunction"
// -----------------------------------------------------------------------------------------------------------------------------------------
#define oMAX_FILE_SIZE (1024*1024*(10*5))
#define oReadFileMod		 'r'
#define oWriteFileMod		 'w'
#define oAppendFileMod       'a'
#define oReadBinaryFileMod   'rb'
#define oWriteBinaryFileMod  'wb'
#define oAppendBinaryFileMod 'ab'
#define oFileOpenStandardFunc "omg_openfile"
#define oDefaultFileMod      'r'
// -----------------------------------------------------------------------------------------------------------------------------------------
#define FastDecVar 1
#ifndef OMGTypesSupport
#	define OMGTypesSupport 1
#endif
#ifndef OMGStandardLib
#	define OMGStandardLib 1
#endif
#ifndef OMGTypesSupport
#	define OMGPy3Support 1
#endif
#ifdef __cplusplus
extern "C" {
#endif
	struct omgtype;
	struct oFunction;
	struct omgf_func;
	struct omgfunc;
	typedef omgtype,omgfunc,omgf_func,oFuntion;
	omgf_func omg_create_func_var(oFunction args);
	omgfunc omg_create_func(char* Fcode,char* funcName);
	


	struct omgtype { // Uses 15 type declaration
		const int* code;
		char*      tname;
		omgtype*   OMGType;
	};
	struct omgtype;
	struct oFunction { // OmgFunction Args
		bool     callwargs;
		char*    argsn;
		omgtype* argst;

	};

	struct omgfunc {
		char*      code;
		char*      funcn;
		const int* fcode;


	};
	struct omgfile_t {
		char*         path;
	    long long int filesize;
		char*         content;
		const char    mode;
	};
	struct omgf_func {
		omgfunc func;
		oFunction args;
	};
	typedef omgtype,omgfunc,omgf_func;
	omgf_func *omg_create_func_warg(oFunction args,omgfunc func_) {
		struct omgf_func* out;
		out->func = func_;
		out->args = args;
		return out;
	}
	omgfunc omg_create_func(char* Fcode, char* funcName) {
		srand(<int>time());
		int func_code = rand();
		if (OMGTypesSupport) {
			struct omgf_func out;
			struct omgfunc func;
			func.fcode = &func_code;
			func.code = Fcode;
			func.funcn = funcName;
			struct oFunction args;
			args.callwargs = false;
			out.func = func;
			out.args = args;
			return out;
		}
		else {
			exit(0); //TODO: Need Some Exception Error Handler
		}
	}


#ifdef __cplusplus
}
#endif